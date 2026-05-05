---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["Runtime Containers", "Kubernetes Core"]
speakers: ["Flavio Castelli", "SUSE"]
sched_url: https://kccnceu2022.sched.com/event/ytoY/what-if-kube-apiserver-could-be-extended-via-webassembly-flavio-castelli-suse
youtube_search_url: https://www.youtube.com/results?search_query=What+If...+Kube-Apiserver+Could+be+Extended+Via+WebAssembly%3F+CNCF+KubeCon+2022
slides: []
status: parsed
---

# What If... Kube-Apiserver Could be Extended Via WebAssembly? - Flavio Castelli, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Flavio Castelli, SUSE
- Schedule: https://kccnceu2022.sched.com/event/ytoY/what-if-kube-apiserver-could-be-extended-via-webassembly-flavio-castelli-suse
- Busca YouTube: https://www.youtube.com/results?search_query=What+If...+Kube-Apiserver+Could+be+Extended+Via+WebAssembly%3F+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre What If... Kube-Apiserver Could be Extended Via WebAssembly?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytoY/what-if-kube-apiserver-could-be-extended-via-webassembly-flavio-castelli-suse
- YouTube search: https://www.youtube.com/results?search_query=What+If...+Kube-Apiserver+Could+be+Extended+Via+WebAssembly%3F+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4CKcMZySUbc
- YouTube title: What If... Kube-Apiserver Could be Extended Via WebAssembly? - Flavio Castelli, SUSE
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/what-if-kube-apiserver-could-be-extended-via-webassembly/4CKcMZySUbc.txt
- Transcript chars: 22415
- Keywords: webassembly, server, inside, assembly, policies, policy, keyboard, binary, instead, container, admission, written, module, running, cannot, controller, create, write

### Resumo baseado na transcript

hi everybody i'm flabby castelli from suzy rancher i'm here today to talk about this crazy idea about extending the kubernetes control plane using webassembly so for the ones who are not familiar with webassembly webassembly is a binary instruction format that means you can pick your favorite programming language write some code and then compile this code into what is being called a webassembly module so instead of building a linux binary for the intel architecture you are instead targeting the web assembly architecture so web assembly is already

### Excerpt da transcript

hi everybody i'm flabby castelli from suzy rancher i'm here today to talk about this crazy idea about extending the kubernetes control plane using webassembly so for the ones who are not familiar with webassembly webassembly is a binary instruction format that means you can pick your favorite programming language write some code and then compile this code into what is being called a webassembly module so instead of building a linux binary for the intel architecture you are instead targeting the web assembly architecture so web assembly is already being supported by many programming languages and more are more of them are currently working towards you know supporting webassembly it's actually a great time for web assembly there is a lot of momentum the reason is because webassembly is a is a pretty interesting technology with many advantages so let's take a closer look at these web assembly modules so the first thing you will notice about them is that they are pretty small so these are small independent computational units that take a really little space and this is i think particularly refreshing you know considering you know how much space it takes a linux container for example these webassembly modules in addition to being small they're also portable that means i can write some code compile that let's say on my apple silicon machine i have a webassembly module and then ship this small webassembly module into i don't know a linux machine running on the intel architecture and then just run it that's because there is a thin abstraction layer in between the web assembly module and the operating system which is the web webassembly runtime webassembly runtimes historically speaking have been placed inside of the browser because web assembly has been a technology created for web application development but nowadays this is no longer true and as a matter of fact there are ways to run webassembly outside of a browser and we will come back to that later so there is one interesting point here given that web assembly was conceived as a technology for the web there are some nice side effects the first one is security so if you think about that when you visit a web page with your browser and this web page has a web assembly module inside of it your web browser is going to download this binary blob from the internet and then it's going to run it on your local machine does it sound scary to you a bit uh luckily when drafting up the web assembly specification a lot of ef
