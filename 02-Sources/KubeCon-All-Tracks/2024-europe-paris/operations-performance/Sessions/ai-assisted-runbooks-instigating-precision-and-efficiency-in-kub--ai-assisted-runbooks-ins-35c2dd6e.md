---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Vinothini Raju", "gopaddle.io", "Larry Carvalho", "RobustCloud"]
sched_url: https://kccnceu2024.sched.com/event/1YeMF/ai-assisted-runbooks-instigating-precision-and-efficiency-in-kubernetes-operations-vinothini-raju-gopaddleio-larry-carvalho-robustcloud
youtube_search_url: https://www.youtube.com/results?search_query=AI-Assisted+Runbooks+-+Instigating+Precision+and+Efficiency+in+Kubernetes+Operations+CNCF+KubeCon+2024
slides: []
status: parsed
---

# AI-Assisted Runbooks - Instigating Precision and Efficiency in Kubernetes Operations - Vinothini Raju, gopaddle.io & Larry Carvalho, RobustCloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Vinothini Raju, gopaddle.io, Larry Carvalho, RobustCloud
- Schedule: https://kccnceu2024.sched.com/event/1YeMF/ai-assisted-runbooks-instigating-precision-and-efficiency-in-kubernetes-operations-vinothini-raju-gopaddleio-larry-carvalho-robustcloud
- Busca YouTube: https://www.youtube.com/results?search_query=AI-Assisted+Runbooks+-+Instigating+Precision+and+Efficiency+in+Kubernetes+Operations+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre AI-Assisted Runbooks - Instigating Precision and Efficiency in Kubernetes Operations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMF/ai-assisted-runbooks-instigating-precision-and-efficiency-in-kubernetes-operations-vinothini-raju-gopaddleio-larry-carvalho-robustcloud
- YouTube search: https://www.youtube.com/results?search_query=AI-Assisted+Runbooks+-+Instigating+Precision+and+Efficiency+in+Kubernetes+Operations+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=82ACSa5ktL8
- YouTube title: AI-Assisted Runbooks - Instigating Precision and Efficiency in Kubernetes Operations
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/ai-assisted-runbooks-instigating-precision-and-efficiency-in-kubernete/82ACSa5ktL8.txt
- Transcript chars: 27744
- Keywords: actually, prompt, operations, troubleshooting, pipeline, context, anything, create, resources, presentation, across, question, information, control, issues, solution, version, template

### Resumo baseado na transcript

good afternoon thank you for coming to this session my name is Larry Calo I'm filling in for Diane mu another speaker but I'm going to just introduce vinotini Raju uh who is the women winner of the women B2B Tech award last year and she's going to present a fantastic slide deck and a demo on Genna in operations so with that we know is going to introduce herself and introduce the slides and the concept and I'm sure you're going to go from out from here with a rack pipeline so this is what uh Lama 2 responded it came up with three solutions check the container has enough memory which is nothing uh related to the problem verify that Java command is currently uh configured again it's not related then check the

### Excerpt da transcript

good afternoon thank you for coming to this session my name is Larry Calo I'm filling in for Diane mu another speaker but I'm going to just introduce vinotini Raju uh who is the women winner of the women B2B Tech award last year and she's going to present a fantastic slide deck and a demo on Genna in operations so with that we know is going to introduce herself and introduce the slides and the concept and I'm sure you're going to go from out from here with a lot of good information on how to use gen in operations you know up to you thank you so much Larry uh for a great introduction hello everyone very good afternoon looks like we have a full room here I'm so excited to see you all and I'll try my best to keep up to the expectations so what are we going to talk today um jna wow that's a happening thing now and we we are all in the kuet space and I'm trying to put these two technologies together so I'm going to be talking about using jna to instigate precision and efficiency in kubernetes operations that's a pretty loaded topic so what I have done is um you know created a short agenda to give you a heads up on what I'll be covering um over the next 20 minutes so I'll do a short introduction to the kubernetes landscape and the G and talk about some of the challenges and the solutions that are available today and I'm going to propose an AI governance framework uh for it uh operations and I'll walk you through a uh you know a troubleshooting use case with a simple uh you know kubernetes issue and then uh show you a complete solution demo of how this whole thing will fit in followed by a quick um Q&A so just a a quick word about who we are so we are a loc Cod uh platform company uh we building an ID for kubernetes making things simpler for um kuers users uh we are headquartered in Bangalore but I I I live in Canada and um we have a distributed team we started off as a devops consulting firm offering cicd automation for uh retail customers across India and us and we also parall contributed and um maintain this project called configurator which um helps you Version Control uh config maps and secrets on kubernetes so since 2017 we are all platform company and we are on different different marketplaces thanks to all our partners so we have about 1,600 plus downloads across all these uh Marketplace um distributions let's dive in um AI for kubernetes what's the necessity and how AI can help so this is a slightly an outdated survey that was conducted by cncf in 2022 u
