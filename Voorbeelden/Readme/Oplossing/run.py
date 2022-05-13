from Voorbeelden import create_app

if __name__ == "__main__":
    app = create_app()
    print("Running on http://127.0.0.1:5000/ ")
    app.run(debug=True, use_reloader=False) # , use_reloader=False