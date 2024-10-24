for ((i = 0; ; i++)); do
  ./a.out
  git add .
  git commit -m "commit"
  # every 50 time, push the commit
  if [[ $((i % 50)) -eq 0 ]]; then
    git push
  fi
done
