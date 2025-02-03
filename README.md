#   PAG BACKEND
just fasapi coupled with mongo

## geting started
clone repo
```bash

```
create an .env with this structure as in the env sample
```
MONGO_USER=""
MONGO_PASSWORD=""
MONGO_DB_NAME=""
MONGO_URL=""
SECRET_KEY=""
```
create a virtual environment
```bash
    python3 -m venv venv
    source venv/bin/activate
```
install requiremnts
```bash
    pip install -r requirements.txt
```

run the server. <br/> run from root directory of source code
```bash
    uvicorn app.main:app --host="0.0.0.0" --port=9935
```

test the swagger docs at /docs