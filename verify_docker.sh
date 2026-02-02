#!/bin/bash
set -e

IMAGE_TAG=$(grep IMAGE_TAG kicks_sniper.config | cut -d'=' -f2)

echo "DEBUG: IMAGE_TAG=$IMAGE_TAG"
echo "DEBUG: docker images | grep -E \"kicks-sniper[[:space:]]+$IMAGE_TAG\""
docker images | grep "kicks-sniper"

if docker images --format "{{.Repository}}:{{.Tag}}" | grep "kicks-sniper:${IMAGE_TAG}" > /dev/null; then
  echo "找到 kicks-sniper:${IMAGE_TAG}，跳過 build。"
else
  echo "沒找到 kicks-sniper:${IMAGE_TAG}，進行 build。"
  IMAGE_TAG=${IMAGE_TAG} docker compose build kicks-sniper-build
fi

echo "驗證 kicks-sniper-crawler 啟動 ..."
IMAGE_TAG=${IMAGE_TAG} docker compose up -d kicks-sniper-crawler
sleep 10
docker compose logs kicks-sniper-crawler

echo "驗證 kicks-sniper-etl 啟動 ..."
IMAGE_TAG=${IMAGE_TAG} docker compose up -d kicks-sniper-etl
sleep 10
docker compose logs kicks-sniper-etl

echo "驗證 kicks-sniper-all 啟動 ..."
IMAGE_TAG=${IMAGE_TAG} docker compose up -d kicks-sniper-all
sleep 10
docker compose logs kicks-sniper-all

echo "驗證完成，請檢查 logs 與 data/raw/kicks_list.json 是否產生。"

docker compose down