#!/usr/bin/env bash
set -euo pipefail

mode="${1:-build}"
quartz_ref="${QUARTZ_REF:-v4}"
quartz_dir="${QUARTZ_DIR:-.quartz}"

case "$mode" in
  build | serve) ;;
  *)
    echo "usage: $0 [build|serve]" >&2
    exit 2
    ;;
esac

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync is required to prepare Quartz content" >&2
  exit 1
fi

if [ ! -d "$quartz_dir/.git" ]; then
  git clone --depth 1 --branch "$quartz_ref" https://github.com/jackyzha0/quartz.git "$quartz_dir"
else
  git -C "$quartz_dir" fetch --depth 1 origin "$quartz_ref"
  git -C "$quartz_dir" checkout "$quartz_ref"
fi

rm -rf "$quartz_dir/content"
mkdir -p "$quartz_dir/content"

rsync -a --delete --prune-empty-dirs \
  --exclude='/.git/**' \
  --exclude='/.github/**' \
  --exclude='/.quartz/**' \
  --exclude='/bin/**' \
  --exclude='/node_modules/**' \
  --exclude='/public/**' \
  --exclude='/scripts/**' \
  --exclude='/_sources/**' \
  --exclude='/05-Templates/**' \
  --include='*/' \
  --include='*.md' \
  --exclude='*' \
  ./ "$quartz_dir/content/"

cp .github/quartz/quartz.config.ts "$quartz_dir/quartz.config.ts"
cp .github/quartz/quartz.layout.ts "$quartz_dir/quartz.layout.ts"

(
  cd "$quartz_dir"
  npm ci
  if [ "$mode" = "serve" ]; then
    npx quartz build --directory content --output public --serve
  else
    npx quartz build --directory content --output public --concurrency 2
  fi
)
