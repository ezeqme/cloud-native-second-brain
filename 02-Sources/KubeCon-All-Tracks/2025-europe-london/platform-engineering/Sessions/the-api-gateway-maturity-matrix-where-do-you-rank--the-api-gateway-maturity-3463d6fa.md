---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Networking"]
speakers: ["Joel Hans", "ngrok"]
sched_url: https://kccnceu2025.sched.com/event/1tx7N/the-api-gateway-maturity-matrix-where-do-you-rank-joel-hans-ngrok
youtube_search_url: https://www.youtube.com/results?search_query=The+API+Gateway+Maturity+Matrix%3A+Where+Do+You+Rank%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The API Gateway Maturity Matrix: Where Do You Rank? - Joel Hans, ngrok

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Networking]]
- País/cidade: United Kingdom / London
- Speakers: Joel Hans, ngrok
- Schedule: https://kccnceu2025.sched.com/event/1tx7N/the-api-gateway-maturity-matrix-where-do-you-rank-joel-hans-ngrok
- Busca YouTube: https://www.youtube.com/results?search_query=The+API+Gateway+Maturity+Matrix%3A+Where+Do+You+Rank%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The API Gateway Maturity Matrix: Where Do You Rank?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7N/the-api-gateway-maturity-matrix-where-do-you-rank-joel-hans-ngrok
- YouTube search: https://www.youtube.com/results?search_query=The+API+Gateway+Maturity+Matrix%3A+Where+Do+You+Rank%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EOQ8qNstD8I
- YouTube title: The API Gateway Maturity Matrix: Where Do You Rank? - Joel Hans, ngrok
- Match score: 0.94
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-api-gateway-maturity-matrix-where-do-you-rank/EOQ8qNstD8I.txt
- Transcript chars: 28442
- Keywords: gateway, maturity, couple, trying, better, everything, problems, developer, platform, little, infrastructure, features, whether, certain, conversation, important, governance, observability

### Resumo baseado na transcript

I know uh this is the last session of the day before cube crawl, so we're going to try to keep it on time. So I want to start with a story that I hope uh will like unfortunately resonate with many of you. Like which is going to provide you the hard the highest ROI right now based on the problems you're facing. It's about evaluating the landscape of capabilities ahead of you and comparing that to what your company actually needs right now and knowing whether you need to solve problem A uh tomorrow because you need to prioritize problem Z today. Uh this is a a model started a couple years ago uh based on uh these five levels of build, operate, scale, improve, and adapt. Operate is that you've moved into uh production scale you're you know playing around with automation githops CI/CD improve is that you're defining security and policy and governance governance across your environment and adapt being that you are kind of futurep proofing your cloudnative uh

### Excerpt da transcript

Thanks everybody for coming. I know uh this is the last session of the day before cube crawl, so we're going to try to keep it on time. Uh and uh super appreciate everybody coming by. Um today we're going to talk about an API gateway maturity matrix. Um my name is Joel Hans. Uh I do a lot of Debell things at Enro. Um and I love stories. So I want to start with a story that I hope uh will like unfortunately resonate with many of you. Uh, so it all starts with a little baby Kubernetes cluster. It's so cute and full of promise. Uh, maybe there's some like OG services. Doesn't matter what the languages. I just Python looks nice up there. Um, and maybe there's a marketing site as well that you get set up. Um, you don't like to you like to have make yourself uh have harder problems than they should be. So you don't just use like S3 and CloudFront. You want to do it all yourself. Uh, and then Oh, okay. Okay, I think there was supposed to be some services that pop in here. Um, let's go back through. Nope, that's not what it's supposed to do at all.

Anyways, you have some Go services that come in at some point. Uh, and then you hire a marketing team and they want to rip out a bunch of the existing website uh, and they want to host that on an external service. And so then you have to figure out how do I host that on the slashblog path? Do I use my cluster as a reverse proxy or do I stand something else up? Uh, and then comes in another project to set up developer documentation again. You don't want to rip everything apart. So, you got to figure out some more routing. Uh, and then you have some more Go services that just don't feel like showing up for me today. Uh, and then you need to move a couple APIs around. Maybe you need to deprecate one V1 to V2, maybe some rewrites, redirects, everything like that. and all of a sudden everything becomes a moving target. They finally worked. Um, and you know, trying to take back control of all of this, trying to make it feel better, work better, it often seems insurmountable. Uh, and if you are a CTO or you are an engineering leader, um, you don't want to be in this position.

Uh, if you're a platform engineer, your path, your golden path doesn't feel so much golden as it does, I don't know, like covered with a rock slide. Uh, and if you are a infrastructure or DevOps engineer, um, you're you're that like this is fine dog meme until you decide to hang up your hat and move into something else. And this is a story of people who
