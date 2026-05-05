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
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Miley Fu", "Second State"]
sched_url: https://kccncna2024.sched.com/event/1i7rB/cloud-native-ai-wasm-in-portable-secure-aiml-workloads-miley-fu-second-state
youtube_search_url: https://www.youtube.com/results?search_query=Cloud-Native+AI%3A+Wasm+in+Portable%2C+Secure+AI%2FML+Workloads+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cloud-Native AI: Wasm in Portable, Secure AI/ML Workloads - Miley Fu, Second State

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Salt Lake City
- Speakers: Miley Fu, Second State
- Schedule: https://kccncna2024.sched.com/event/1i7rB/cloud-native-ai-wasm-in-portable-secure-aiml-workloads-miley-fu-second-state
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud-Native+AI%3A+Wasm+in+Portable%2C+Secure+AI%2FML+Workloads+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cloud-Native AI: Wasm in Portable, Secure AI/ML Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rB/cloud-native-ai-wasm-in-portable-secure-aiml-workloads-miley-fu-second-state
- YouTube search: https://www.youtube.com/results?search_query=Cloud-Native+AI%3A+Wasm+in+Portable%2C+Secure+AI%2FML+Workloads+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UY9VxVgAsEg
- YouTube title: Cloud-Native AI: Wasm in Portable, Secure AI/ML Workloads - Miley Fu & Michael Yuan, Second State
- Match score: 0.839
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cloud-native-ai-wasm-in-portable-secure-ai-ml-workloads/UY9VxVgAsEg.txt
- Transcript chars: 24208
- Keywords: language, models, application, python, machine, translation, gpu, chinese, english, github, support, wasm, running, couple, source, answer, lightweight, multiple

### Resumo baseado na transcript

uh hi everyone Welcome to our talk today so uh today our topic is to use web assembly to run AI influence um so um I am the founding member of wasm Ed project as you can see um on the slides that that's our GitHub repo it's a cncf project and Mel is a Founder uh of this project was match uh so so I think we will start with two demos um we are going to run open source gen models on your infra and or boundled with it become become I think a huge problem for portability right you know that then of course you know people um are not really interested in working with C++ anymore especially application developers you know I think rust and go would be the languages would

### Excerpt da transcript

uh hi everyone Welcome to our talk today so uh today our topic is to use web assembly to run AI influence um so um I am the founding member of wasm Ed project as you can see um on the slides that that's our GitHub repo it's a cncf project and Mel is a Founder uh of this project was match uh so so I think we will start with two demos um we are going to run open source gen models on your infra and or boundled with your own apps thank you Mary yeah so yeah I think the best way to get started instead of explaining what is wasam and why we use it for AI and all kind of stuff you know I think it's probably easier if we just have a demo to see what we can do and what are the benefit why why why don't you use Python why don't you use AMA why don't you use any of the other large language model model toolkit out there so um here is a GitHub report that we prepared it's called Talk talk you know so let me actually um exit from here and uh uh please excuse my Messi La desktop it's here so I going to run this demo twice you know um if you look at this UI this is um you know uh a lot of you may be familiar with this with this UI it's a it's a web UI and it allow me to talk to my computer and uh then it would generate some answer so let me talk to my computer now I had record I mean Sol City right now can you recommend some places to Wi it so hopefully that you heard my question right I said I'm in Salt Lake City right now can you recommend some places to visit and I going to submit it you know so basically it send this voice to a server it's come back right back okay so you know so here say I'm transcribed to I'm inan Sal Lake City can you recommend some place to wear that and here is the answer in text and also in voice so I play the voice and let you hear Utah state capital Natural History Museum of Utah and Great Salt Lake also check out the Gateway Mall redb Garden and nen Peak all right so you know um so this is um you know it's seem like a basic application right you know just uh transcribe voice text use a large language model to answer the text and then sensitize the text back to W okay so um but uh what I want to focus on is that this the whole setup requires very little resources this whole setup runs on the lowest GPU machine you can buy you can possibly buy on Azure so it's on media T4 it runs three J models with their own wrong time with their own PRS and with the entire application is just running on a single GPU machine right so this is the first demo and
