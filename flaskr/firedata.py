import firebase_admin
from firebase_admin import credentials, db, firestore

cred = credentials.Certificate("../nuvomemo-backend-firebase-adminsdk-4rwbr-9209e4a798.json")
# firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection("users").get()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")