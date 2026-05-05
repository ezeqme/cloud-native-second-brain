---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Yuhan Liu", "University of Chicago", "Suraj Deshmukh", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27FcQ/llms-on-kubernetes-squeeze-5x-gpu-efficiency-with-cache-route-repeat-yuhan-liu-university-of-chicago-suraj-deshmukh-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=LLMs+on+Kubernetes%3A+Squeeze+5x+GPU+Efficiency+With+Cache%2C+Route%2C+Repeat%21+CNCF+KubeCon+2025
slides: []
status: parsed
---

# LLMs on Kubernetes: Squeeze 5x GPU Efficiency With Cache, Route, Repeat! - Yuhan Liu, University of Chicago & Suraj Deshmukh, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Yuhan Liu, University of Chicago, Suraj Deshmukh, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27FcQ/llms-on-kubernetes-squeeze-5x-gpu-efficiency-with-cache-route-repeat-yuhan-liu-university-of-chicago-suraj-deshmukh-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=LLMs+on+Kubernetes%3A+Squeeze+5x+GPU+Efficiency+With+Cache%2C+Route%2C+Repeat%21+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre LLMs on Kubernetes: Squeeze 5x GPU Efficiency With Cache, Route, Repeat!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FcQ/llms-on-kubernetes-squeeze-5x-gpu-efficiency-with-cache-route-repeat-yuhan-liu-university-of-chicago-suraj-deshmukh-microsoft
- YouTube search: https://www.youtube.com/results?search_query=LLMs+on+Kubernetes%3A+Squeeze+5x+GPU+Efficiency+With+Cache%2C+Route%2C+Repeat%21+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2YCDvZokqnk
- YouTube title: LLMs on Kubernetes: Squeeze 5x GPU Efficiency With Cache, Route, Repea... Yuhan Liu & Suraj Deshmukh
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/llms-on-kubernetes-squeeze-5x-gpu-efficiency-with-cache-route-repeat/2YCDvZokqnk.txt
- Transcript chars: 23121
- Keywords: request, engine, inference, router, gpu, memory, decode, prefill, replica, performance, offloading, improve, question, prompt, results, prefiller, decoder, requests

### Resumo baseado na transcript

Um, welcome to the talk uh, LLMs on Kubernetes squeeze 5x GPU efficiency with cache route and repeat. I'm a fifth year PhD student at the University of Chicago working on system for machine learning. Um we'll we'll we'll see more there have been a lot of talks that have gone into the depths of each of uh like what these metrics are. So uh let's see like a query like what happens like in a query's uh lifetime right uh so the like when you send those when you send that prompt uh like all those tokens are loaded at once and while that while the while And with with uh each word there is associated key and value metrics behind the scene and that's generated per transformer layer. So the challenges of vanilla approach right like like what whatever we saw so far that's that's vanilla there are no optimizations uh here so it all of this is fine when there are few requests but as concurrent requests show up the and long

### Excerpt da transcript

Awesome. Um, welcome to the talk uh, LLMs on Kubernetes squeeze 5x GPU efficiency with cache route and repeat. I know it's the probably the last talk of the day. Uh, thanks. I'm really grateful to everyone who showed up here. All right, cool. Uh, let's start. Uh, I'm Suraj. I work as a principal software engineer at Microsoft. Um, and yeah. >> Hi everyone. I'm Yuan. I'm a fifth year PhD student at the University of Chicago working on system for machine learning. >> All right, cool. Uh before we talk about any efficiency or anything like that, let's first like get some basics clear, right? So what's what's inference that the diagram that you see it's just a placeholder I I would say like you'd see there's a client a pod running on node and that pod is occupying all the GPUs there is a sample request going back and forth so uh okay so what's inference right inference is uh just a forward pass of the of the model so there are no gradient updates just just the prediction and it's it's like it's like running the any other micros service on on Kubernetes right u instead of instead of just uh handling API requests what it's doing is it's there is it's generating text token at a time and as each request like grows u as in when the output grows sequentially it's uh the latency also accumulates and then that's that's the whole generation process and uh since each request is like long running it it's behind the scene it's also consuming the GPU memory that's why like all the GPU efficiency matters and the the the analogy that I like to give is uh think of think of uh model training like building docker images and serving like using those docker images on on on kubernetes so and and before we understand uh like how to gain the efficiency.

Let's see what metrics we are trying to optimize. One is the throughput. Throughput is token per second of whatever the deployment system looks like. So we are trying to maximize that and the other is time to first token. Uh we are trying to minimize time to first token. So if you ask what time to first token is you know how you like write a prompt in chat GPT and then you wait for some time before the the first word shows up. So that time between sending that request and waiting for the first word that's the time to first token. Um we'll we'll we'll see more there have been a lot of talks that have gone into the depths of each of uh like what these metrics are. Uh I have a slide at the end that you can you know take a picture later
