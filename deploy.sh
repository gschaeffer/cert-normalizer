sed -i '' 's/debug=True/debug=False/g' wsgi.py


export PROJECT=$(gcloud config get-value project | tr ':' '/')

gcloud run deploy normalizer \
    --source . \
    --allow-unauthenticated \
    --region=us-central1 \
    --service-account=web-service@$PROJECT.iam.gserviceaccount.com

# --ingress internal-and-cloud-load-balancing \

sed -i '' 's/debug=False/debug=True/g' wsgi.py