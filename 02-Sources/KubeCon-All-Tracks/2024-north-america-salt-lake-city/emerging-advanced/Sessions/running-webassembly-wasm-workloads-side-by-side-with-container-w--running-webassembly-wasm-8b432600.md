---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Jiaxiao Zhou", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1i7oH/running-webassembly-wasm-workloads-side-by-side-with-container-workloads-jiaxiao-zhou-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Running+WebAssembly+%28Wasm%29+Workloads+Side-by-Side+with+Container+Workloads+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Running WebAssembly (Wasm) Workloads Side-by-Side with Container Workloads - Jiaxiao Zhou, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: United States / Salt Lake City
- Speakers: Jiaxiao Zhou, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1i7oH/running-webassembly-wasm-workloads-side-by-side-with-container-workloads-jiaxiao-zhou-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Running+WebAssembly+%28Wasm%29+Workloads+Side-by-Side+with+Container+Workloads+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Running WebAssembly (Wasm) Workloads Side-by-Side with Container Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oH/running-webassembly-wasm-workloads-side-by-side-with-container-workloads-jiaxiao-zhou-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Running+WebAssembly+%28Wasm%29+Workloads+Side-by-Side+with+Container+Workloads+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Bq5aTYyRBH0
- YouTube title: Running WebAssembly (Wasm) Workloads Side-by-Side with Container Workloads - Jiaxiao Zhou, Microsoft
- Match score: 0.942
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/running-webassembly-wasm-workloads-side-by-side-with-container-workloa/Bq5aTYyRBH0.txt
- Transcript chars: 27614
- Keywords: assembly, container, containers, application, binary, components, running, question, called, memory, component, function, request, runtime, dapper, instance, execute, handler

### Resumo baseado na transcript

all right let's uh get started quick poll here raise your hand if you have ever compiled your application to web assembly before okay I saw a few and keep your hands raised up if you ever compelled web assembly to deploy web assembly to uh production clusters on kubernetes okay I see a bit of drop off there not surprising and today I want to make a case for web assembly as alternative to Containers or even as a partner for containers and we'll do this as a case and it can run web assem side by side with containers how do we do that well the magic lies in the shim architecture when continuity gives a ttrpc request into the shim asking the shim to create a container and start executing the container Json is it's just order ID 42 um and I can get a new order and they changed to 42 so this is to demonstrate this state engine behave similar to the Dapper engine and now when I distribute this wi and binary into the

### Excerpt da transcript

all right let's uh get started quick poll here raise your hand if you have ever compiled your application to web assembly before okay I saw a few and keep your hands raised up if you ever compelled web assembly to deploy web assembly to uh production clusters on kubernetes okay I see a bit of drop off there not surprising and today I want to make a case for web assembly as alternative to Containers or even as a partner for containers and we'll do this as a case study for web assembly and containers to run side by side and we will see how web assembly can be this uh next ground breaking technology and my name is Joe I'm a soft engineer Microsoft Azure and I build open source software I'm a maintainer of the cncf contained the run Wazi project and I also maintain the spin Cube and I'm a recognized contributor of The Bu code Alliance you can reach out to my socials um I have LinkedIn GitHub and X where are we going today first I want to talk about the concept of Scar containers and their motivations and use cases and then I will talk about web assembly and how it compare in contrast to containers and then I will do it C in action uh running web assembly with SARS as SARS and I will do some future forward uh conclusion and in the last five minutes we will do Q&A all right so cyar containers are a old Concept in kubernetes it was introduced in 2015 um and the cyar term was refer to a auxiliary container running alongside your main application in the same PA and because they are running in the same part so they share the same name spaces in particular the network namespace and c groups and those cyar containers um obviously by their name they're lightweight and they're smaller than your main application and they're providing additional features to guide your main application such as logging monitoring and networking and in kubernetes uh v 1.29 as a beta feature they formally introduce cyard containers as in neque containers while you have to specify the resar policy to be always there are some interesting cyer use cases there's logging use case uh if you can deploy your open slam CH collector as a scar container to your main application obviously there is serice smash and one more interesting use case is called Dapper uh which is another cncf project that gives you long time application apis such as State Management servicing locations and message cues there are some downsides to the scar containers though for one scars could be heavyweight and one example would
