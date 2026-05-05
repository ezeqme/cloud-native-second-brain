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
themes: ["Runtime Containers", "SRE Reliability"]
speakers: ["Michael Yuan", "Second State"]
sched_url: https://kccnceu2024.sched.com/event/1YeQM/fast-and-efficient-log-processing-with-wasm-and-ebpf-michael-yuan-second-state
youtube_search_url: https://www.youtube.com/results?search_query=Fast+and+Efficient+Log+Processing+with+Wasm+and+eBPF+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Fast and Efficient Log Processing with Wasm and eBPF - Michael Yuan, Second State

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Michael Yuan, Second State
- Schedule: https://kccnceu2024.sched.com/event/1YeQM/fast-and-efficient-log-processing-with-wasm-and-ebpf-michael-yuan-second-state
- Busca YouTube: https://www.youtube.com/results?search_query=Fast+and+Efficient+Log+Processing+with+Wasm+and+eBPF+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Fast and Efficient Log Processing with Wasm and eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQM/fast-and-efficient-log-processing-with-wasm-and-ebpf-michael-yuan-second-state
- YouTube search: https://www.youtube.com/results?search_query=Fast+and+Efficient+Log+Processing+with+Wasm+and+eBPF+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4u7nUpZxr3g
- YouTube title: Fast and Efficient Log Processing with Wasm and eBPF - Michael Yuan, Second State
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/fast-and-efficient-log-processing-with-wasm-and-ebpf/4u7nUpZxr3g.txt
- Transcript chars: 32989
- Keywords: wasm, container, application, applications, processing, server, ebpf, deploy, containers, deployment, machine, process, native, meaning, microservices, database, called, isolation

### Resumo baseado na transcript

all right okay so um I think it's time so let's get started um well um thank you all for being here you know I'm really glad to see so many people are interested in this topic and uh um you know uh Cube accounts have you know earlier deadlines for the uh for the talk so when I submitted the talk I want to talk about log processing but when I thought about it when I write up the the slides I thought you know it's really about stream we have just mentioned the kubernetes container um uh Linux container for Linux containers are not are uh are not truly cross platform so you need to give it a CPU architecture right you know it's X8 or um 64 you know whatever so there's a new um CPU architecture called Web assembly WM 32 okay so when you when you have a wasm binary artifact you build a wasm application to build a wasm binary B code application sort of like Java Bal application right you can upload it

### Excerpt da transcript

all right okay so um I think it's time so let's get started um well um thank you all for being here you know I'm really glad to see so many people are interested in this topic and uh um you know uh Cube accounts have you know earlier deadlines for the uh for the talk so when I submitted the talk I want to talk about log processing but when I thought about it when I write up the the slides I thought you know it's really about stream processing not just limited logs about other things so you know uh my name is Michael Yan and I'm the maintainer of cnf's um web some long time project called wasm Ed so that's a a GitHub link if you're interested you know um withit us on on GitHub you know there's essentially all activities happening over there so um as you can see the title you know there's two seemingly unrelated technology that be mentioned in the same sentence wasm and ebpf you know um if I if I ask people most people would just know that both um lightwe meral virtual machine formats but how are they related you know that's that's you know we're going to dive into that and uh we're going to even go further you know we're going to uh towards the end of this talk and we can also talk about things like U you know um Ai and machine learning which seem to be the the the topic of this conference right how does that relat to say wasm and ebpf and uh the whole idea of stream processing right you know so there's a lot of topic we're going to cover um I do have some um some demos but I don't think we have time to do the live demo here so I going to give you the link and uh um and you can you know go home and do that from your hotel room you know that's I think it also would be more friendly to the to the conference band WDS right so you know um from the conversation that I had U yesterday and the the day before that um it seems like um a lot of people are not really familiar with say the cloud native wasm idea you know so web assembly sounds like something you use in the browser you know how's that how's that related with you know um uh Cloud native Computing and what do you mean what do we mean by you know um wasm on the server side so this um this whole idea goes all the way so added a couple slides at the beginning of this talk right so this is one of the slides that added so the idea goes all the way back to the origin of the cloud computing right you know so the cloud is really you know sharing Resources with other people people you know on the on on the larger
