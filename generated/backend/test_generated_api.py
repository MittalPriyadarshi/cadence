def test_generated_app_import():
    import generated.backend.app as app
    assert hasattr(app, 'app')
