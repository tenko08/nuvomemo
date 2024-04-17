import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("nuvomemo-backend-firebase-adminsdk-4rwbr-1d4250d24a.json")
firebase_admin.initialize_app(cred)
