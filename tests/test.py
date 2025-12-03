from keva import keva_mem, keva_str


def _check_backend(backend):
    backend.reset()
    assert backend.get("missing") == ""

    backend.set("a", "1")
    assert backend.get("a") == "1"

    backend.set("a", "2")
    assert backend.get("a") == "2"

    backend.set("b", "3")
    assert backend.get("b") == "3"

    backend.delete("a")
    assert backend.get("a") == ""
    backend.delete("a")

    backend.reset()
    assert backend.get("b") == ""


def test_keva_mem_backend():
    _check_backend(keva_mem)


def test_keva_str_backend():
    _check_backend(keva_str)

