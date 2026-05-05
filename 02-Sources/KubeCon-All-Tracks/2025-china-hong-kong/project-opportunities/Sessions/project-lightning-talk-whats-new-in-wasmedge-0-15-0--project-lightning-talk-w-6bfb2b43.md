---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Michael Yuan", "Maintainer"]
sched_url: https://kccncchn2025.sched.com/event/1xjzT/project-lightning-talk-whats-new-in-wasmedge-0150-michael-yuan-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+WasmEdge+0.15.0%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: What's New in WasmEdge 0.15.0? - Michael Yuan, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: China / Hong Kong
- Speakers: Michael Yuan, Maintainer
- Schedule: https://kccncchn2025.sched.com/event/1xjzT/project-lightning-talk-whats-new-in-wasmedge-0150-michael-yuan-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+WasmEdge+0.15.0%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What's New in WasmEdge 0.15.0?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1xjzT/project-lightning-talk-whats-new-in-wasmedge-0150-michael-yuan-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+WasmEdge+0.15.0%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6OTwwscCUNQ
- YouTube title: Project Lightning Talk: What's New in WasmEdge 0.15.0? - Michael Yuan, Maintainer
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-whats-new-in-wasmedge-0-15-0/6OTwwscCUNQ.txt
- Transcript chars: 6087
- Keywords: support, runtime, models, hardware, switch, students, device, github, needed, abstraction, driver, embedded, lightning, biggest, including, language, interested, runtimes

### Resumo baseado na transcript

So we are a um you know uh our biggest use case today is as a lightweight AI runtime running um different AI models including large language model and uh um and uh um you know audio video and all those on edge device and edge cloud right so uh if you're interested you know we have um you know so those are GitHub links you know so if you're interested take a picture and uh um join us in our GitHub community.

### Excerpt da transcript

So um you probably heard about was edge during the keynote. So we are a um you know uh our biggest use case today is as a lightweight AI runtime running um different AI models including large language model and uh um and uh um you know audio video and all those on edge device and edge cloud right so uh if you're interested you know we have um you know so those are GitHub links you know so if you're interested take a picture and uh um join us in our GitHub community. So um we started um I think five years ago right before the pandemic and uh so at the time we want to do a um uh outside of the browser web assembly environment. Um it has its up and downs. So we we did serless functions and plugins and uh and we joined CNCF at that time as a as a container alternative. Um so we had a we have community have done a lot of work. Um however in the past two years it has been emerging very clearly that wasn't um possess some of the very interesting characteristics that are needed as a AI runtime because it provide abstraction layer uh over you know heterogeneous hardware like the GPUs and also the the runtimes the drivers and you know things like that.

So that allows uh uh using WASM as a abstraction layer allows developers to write their applications compile to WOM and then deploy it on any hardware any any driver and any runtime. So you know so you can target a wide variety of different from Huawei to a media to Mac same binary just to copy the binary or file uh anywhere that you you want to run and you can run it right you know so wom become uh you know the value proposition of wom become that you know becomes abstraction layer on top of um you know all the different hardware and and runtime we see uh you know in front of you know under um for those AI devices and uh um so as of today you know one of the one of our bigger project called llama LMA H. The Lama H provides um you know um uh embedded API servers that's uh fully a uh open eye compatible. So you can run think about you can run open eye embedded in your application and switch the model as needed. Switch the data switch the knowledge base switch things like that as needed and without worrying com worry without worrying about driver dependencies or the runtime dependencies.

Does it does it need metal 4 on the newest Mac or could it use MIX on the older Mac or does it need CUDA 11 or CUDA 12 you know so you don't have to worry about those questions anymore just develop your application and uh have the wat
