def test_import_backend():
    import generated.backend.app as app
    assert hasattr(app,"app")
