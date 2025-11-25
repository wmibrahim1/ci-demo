echo "# Test Commit" >> README.md
git add README.md
git commit -m "Trigger Jenkins build"
git push
