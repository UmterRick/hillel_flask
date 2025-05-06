from api import app


def main():
    app_config={
        'DEBUG': True
    }
    app.config.update(app_config)
    app.run(host='0.0.0.0', port=5300)


if __name__=='__main__':
    main()