# How to add these to your repo

Copy these into the **root** of `Diabetes_Prediction_System`, matching this layout:

```
Diabetes_Prediction_System/
├── api/
│   └── index.py          <-- new
├── static/
│   ├── diabetes_model.pkl
│   ├── scaler.pkl
│   └── style.css
├── templates/
│   └── index.html
├── app.py                <-- unchanged, keep as is
├── requirements.txt      <-- new
└── vercel.json           <-- new
```

## Steps

1. In your local clone of the repo, copy `api/`, `requirements.txt`, and `vercel.json` into the project root (same level as `app.py`).
2. Commit and push:
   ```
   git add api requirements.txt vercel.json
   git commit -m "Add Vercel deployment config"
   git push
   ```
3. In Vercel:
   - Import the repo (or trigger a redeploy if it's already connected).
   - When asked for a framework preset, choose **Other** — don't let it guess Next.js/React.
   - Leave build/output settings as default; Vercel auto-detects Python functions from the `api/` folder.
4. Deploy. Visit the URL Vercel gives you — your form should load and predictions should work exactly like on `localhost`.

## If it still fails

Open the deployment's build/function logs in the Vercel dashboard and check for:
- `ModuleNotFoundError` → a package is missing from `requirements.txt`.
- A crash on `joblib.load(...)` → the `static/diabetes_model.pkl` or `scaler.pkl` file didn't get committed to git (check `git status` — sometimes `.pkl` files get accidentally gitignored).
- `500` on submitting the form but the homepage loads fine → check that `session` (used to store the prediction) is working; Vercel functions are stateless per-request, so if predictions ever act "flaky," that's the likely cause and we can swap `session` for passing the result directly in the render call.
