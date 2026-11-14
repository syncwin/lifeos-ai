import json, os, subprocess, sys, tempfile, unittest, uuid

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "scripts", "log_guard.py")


def tu(name, inp=None):
    return {"message": {"role": "assistant", "content": [{"type": "tool_use", "name": name, "input": inp or {}}]}}


def run(rows, sid=None, extra=""):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "t.jsonl")
        with open(p, "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
            f.write(extra)
        ev = {"transcript_path": p, "session_id": sid or str(uuid.uuid4())}
        r = subprocess.run([sys.executable, "-I", SCRIPT], input=json.dumps(ev), capture_output=True, text=True)
        return r.returncode, r.stdout


LIFE = tu("Skill", {"skill": "lifeos:workos-log"})
EDIT = tu("Write", {"file_path": "x"})
MEM = "mcp__memory__save_progress"


class T(unittest.TestCase):
    def test_non_lifeos_session_silent(self):
        self.assertEqual(run([tu("Skill", {"skill": "fsdevops:x", "args": "lifeos-ai repo"}), EDIT])[1], "")

    def test_blocks_once_per_session(self):
        sid = str(uuid.uuid4())
        rows = [LIFE, EDIT]
        self.assertIn("block", run(rows, sid, extra=MEM)[1])
        self.assertEqual(run(rows, sid, extra=MEM)[1], "")

    def test_memory_save_progress_counts_as_log(self):
        self.assertEqual(run([LIFE, EDIT, tu(MEM)])[1], "")

    def test_no_log_tool_warns_not_blocks(self):
        out = run([LIFE, EDIT])[1]
        self.assertNotIn("block", out)
        self.assertIn("systemMessage", out)

    def test_log_after_edit_ok(self):
        self.assertEqual(run([LIFE, EDIT, tu("mcp__x__log_entry")])[1], "")

    def test_bad_input_fails_open(self):
        r = subprocess.run([sys.executable, "-I", SCRIPT], input="nope", capture_output=True, text=True)
        self.assertEqual((r.returncode, r.stdout), (0, ""))


if __name__ == "__main__":
    unittest.main()
