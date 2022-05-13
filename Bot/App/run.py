from Percistence.configure import Configure
from Domain.DomainController import DomainController
from View import create_app

controller = DomainController()

config = Configure()

if __name__ == "__main__":
    app = create_app()
    print("Running on http://127.0.0.1:5000/ ")
    app.run(debug=True, use_reloader=False) # , use_reloader=False