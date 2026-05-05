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
speakers: ["Yuan Tang", "Red Hat", "Adam Tetelman", "NVIDIA"]
sched_url: https://kccncna2024.sched.com/event/1i7ns/unlocking-potential-of-large-models-in-production-yuan-tang-red-hat-adam-tetelman-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+Potential+of+Large+Models+in+Production+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Unlocking Potential of Large Models in Production - Yuan Tang, Red Hat & Adam Tetelman, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Yuan Tang, Red Hat, Adam Tetelman, NVIDIA
- Schedule: https://kccncna2024.sched.com/event/1i7ns/unlocking-potential-of-large-models-in-production-yuan-tang-red-hat-adam-tetelman-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Unlocking+Potential+of+Large+Models+in+Production+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Unlocking Potential of Large Models in Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ns/unlocking-potential-of-large-models-in-production-yuan-tang-red-hat-adam-tetelman-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Unlocking+Potential+of+Large+Models+in+Production+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oVJXnlrSuDE
- YouTube title: Unlocking Potential of Large Models in Production - Yuan Tang, Red Hat & Adam Tetelman, NVIDIA
- Match score: 0.795
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/unlocking-potential-of-large-models-in-production/oVJXnlrSuDE.txt
- Transcript chars: 33775
- Keywords: actually, models, llm, inference, production, feature, working, around, support, serving, container, features, platform, server, performance, benchmarking, provides, runtime

### Resumo baseado na transcript

hi everyone uh excited to be here uh my name is yanang I'm a principal software engineer at rat working on our hybrid Cloud AI platform and and I'm Adam telman I am from Nvidia I'm a principal product architect and I'm working across or djx djx cloud and trying to do a lot of things Upstream with uh Community software um and so today we're going to talk about llms and llms in production so we both do a lot with generative AI applications and so I think when

### Excerpt da transcript

hi everyone uh excited to be here uh my name is yanang I'm a principal software engineer at rat working on our hybrid Cloud AI platform and and I'm Adam telman I am from Nvidia I'm a principal product architect and I'm working across or djx djx cloud and trying to do a lot of things Upstream with uh Community software um and so today we're going to talk about llms and llms in production so we both do a lot with generative AI applications and so I think when we started putting this together we did not know how many talks there were going to be around llms and generative Ai and rag At cubec Con but it really seems like it's rag con this year every every Talk's been on it so uh what we wanted to do with this talk was first sort of sound set a foundation so I think a lot of talks have gone to a lot of booths they sort of jump into things assuming everyone is on the same page so we're not going to do that I'm going to try to just throw a bunch of reference architectures up there talk about some definitions talk about the problem uh and then talk about more advanced problems that come with production so show show of hands who's who's used a chatbot an llm who's used the llm okay now put your hand down if you have uh not used one that you were running with a Docker container and kubernetes you've all done one okay so now put your hand down or keep your hand up if you have deployed an llm in kubernetes in production okay I still see hands up that's good that's good okay so so so there's a there's this progression here right so we're going to talk about that progression and then we're going to use kerve as a case study to talk about how we've we've sort of solve this progression and then we're going to spend the last few minutes of the talk talking about open problems uh that are unsolved and hopefully if you guys are interested you can help us solve them in the future because we're doing most of this in the open source so what what what does it take to actually do that jump from the the container Docker run or or ol or whatever to a kubernetes deployment that's life cycled well well first there's a lot of components so you you don't just have your llm uh you have an llm model you have the inference server around that model you have uh your whole rag system and that's going to have an a betting model a guard r model a bunch of databases a bunch of data connectors uh and then you're going to have a bunch of stuff on the other side of that that's actually making thos
