---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Abdullah Gharaibeh", "Rupeng Liu", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7rn/distributed-multi-node-model-inference-using-the-leaderworkerset-api-abdullah-gharaibeh-rupeng-liu-google
youtube_search_url: https://www.youtube.com/results?search_query=Distributed+Multi-Node+Model+Inference+Using+the+LeaderWorkerSet+API+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Distributed Multi-Node Model Inference Using the LeaderWorkerSet API - Abdullah Gharaibeh & Rupeng Liu, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Abdullah Gharaibeh, Rupeng Liu, Google
- Schedule: https://kccncna2024.sched.com/event/1i7rn/distributed-multi-node-model-inference-using-the-leaderworkerset-api-abdullah-gharaibeh-rupeng-liu-google
- Busca YouTube: https://www.youtube.com/results?search_query=Distributed+Multi-Node+Model+Inference+Using+the+LeaderWorkerSet+API+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Distributed Multi-Node Model Inference Using the LeaderWorkerSet API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rn/distributed-multi-node-model-inference-using-the-leaderworkerset-api-abdullah-gharaibeh-rupeng-liu-google
- YouTube search: https://www.youtube.com/results?search_query=Distributed+Multi-Node+Model+Inference+Using+the+LeaderWorkerSet+API+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Al51wafTrRE
- YouTube title: Distributed Multi-Node Model Inference Using the LeaderWorkerSet API- Abdullah Gharaibeh, Rupeng Liu
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/distributed-multi-node-model-inference-using-the-leaderworkerset-api/Al51wafTrRE.txt
- Transcript chars: 31546
- Keywords: leader, worker, workers, replica, running, number, serving, inference, single, server, stateful, replicas, distributed, gpu, create, basically, decode, actually

### Resumo baseado na transcript

hi everyone um my name is uh Abdullah and I'm here to present um our work on the leader workers set API for distributed inference um this is a joint work with uh my colleague ruping and um and other uh people in the community so before I get started let's just show hands how many people are familiar with llm serving okay that's good and how many of you are familiar with um distribu multi node multi-host serving okay that's good and how many are familiar with disaggregated serving

### Excerpt da transcript

hi everyone um my name is uh Abdullah and I'm here to present um our work on the leader workers set API for distributed inference um this is a joint work with uh my colleague ruping and um and other uh people in the community so before I get started let's just show hands how many people are familiar with llm serving okay that's good and how many of you are familiar with um distribu multi node multi-host serving okay that's good and how many are familiar with disaggregated serving only three okay and how many of you have a flight at 7:45 okay um so most likely I'm going to run out of here right after this talk I'm sorry very sorry but I had to catch my flight um but I'm really happy to to discuss anything related to distributed inference and leader worker Set uh through our like you know Community uh channels all right so what is the problem we're trying to solve here well large language models are getting bigger and bigger by definition they are large but they're getting larger and larger so we start like right now average model size is 70b like if you ask people they either use 7B Lama for example and now they are more frequently using 70b Lama models those models still fit in the GPU memory um of one or two chaps like if you think about an a100 for example or h100 GPU and a100 for example have like 40 GB of memory right so 7B um uh model uh with um you know uh full Precision for example 16 bit it it can fit easily however now we're crossing that into a new territory even the open moders like we all we already know that for example GPT uh even Gemini they are probably one trillion plus right so that's like that's not a secret but even the open models that we have out there uh are getting larger and so the latest one is Lama 3 405b that meta released um a few months back those models they barely fit the GPU memory of a single machine most machines the largest one for example on any cloud provider you got eight a100 or8 h100 gpus so if you do a math like for 405b you need 800 GB full Precision uh s so that that would not fit the GPU machine um a single GPU machine so instantly you need to have at least two um even if you do like you know quantization and um make it like you know 400 GB size it would fit a single machine but you wouldn't have enough space on the GPU memory to do a lot large enough batches right um and so we expect that this 405p is just also the beginning it's going to continue to grow granted that gpus will have more memory will have bigger
