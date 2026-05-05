---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Keynote Sessions"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Michael Yuan", "WasmEdge"]
sched_url: https://kccncchn2025.sched.com/event/1x5jJ/keynote-an-optimized-linux-stack-for-genai-workloads-michael-yuan-wasmedge
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+An+Optimized+Linux+Stack+for+GenAI+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: An Optimized Linux Stack for GenAI Workloads - Michael Yuan, WasmEdge

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: China / Hong Kong
- Speakers: Michael Yuan, WasmEdge
- Schedule: https://kccncchn2025.sched.com/event/1x5jJ/keynote-an-optimized-linux-stack-for-genai-workloads-michael-yuan-wasmedge
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+An+Optimized+Linux+Stack+for+GenAI+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: An Optimized Linux Stack for GenAI Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5jJ/keynote-an-optimized-linux-stack-for-genai-workloads-michael-yuan-wasmedge
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+An+Optimized+Linux+Stack+for+GenAI+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pQYyv_y8U-E
- YouTube title: Keynote: An Optimized Linux Stack for GenAI Workloads - Michael Yuan, WasmEdge
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-an-optimized-linux-stack-for-genai-workloads/pQYyv_y8U-E.txt
- Transcript chars: 10326
- Keywords: application, applications, models, language, behind, sidecar, answer, hardware, interact, server, inference, workloads, source, running, however, little, almost, native

### Resumo baseado na transcript

So uh my name is Michael Yu and uh so we've heard from Jim that's open source AI has one and we also heard from Chris that's uh you know there new certification program for running AI in the cloud. We also heard from Bill there's new products and you know there's uh many ways to run open source AIS in the cloud. So for applications that build on top of that, portability has again become a huge problem. We thought we have solved this problem almost 20 years ago with you know with first with Java then with Docker but now this problem has become front and center again. There's so many devices that been produced that needs to interact with AI um uh cloud-based AI applications in the manner that is performance critical. And the second biggest second even bigger problem is the primary or the business logic leaks into the sidec car because you need so much interaction between the a uh because AI model and the application you ends up writing a uh you ends up

### Excerpt da transcript

So uh my name is Michael Yu and uh so we've heard from Jim that's open source AI has one and we also heard from Chris that's uh you know there new certification program for running AI in the cloud. We also heard from Bill there's new products and you know there's uh many ways to run open source AIS in the cloud. However, the question has to be asked why is today most cloudnative applications are treating the large language model or AI models as secondclass citizens meaning we are running them inside cars although they are open but behind some kind of obscure API servers or API gateways and not integrating them into our main application logic. So this is the point I want to discuss uh in this keynote how to make them the first class citizen and uh so a little bit about myself. So I'm a maintainer of the was mage project. I contribute to a bunch of open source projects as well. So not that important. So um I think the the reason we run um AI applications um almost as a as a afterthought in our cloud native applications because currently the AI runtime model is very incompatible with the cloud model because what enables the cloud is the portability of the workload of the of the payload, right?

you know because as one of the famous saying has gone you know that's uh you know cloud is just other people's computer so um the the whole cloud development deployment paradigm is that I write applications on my own computer but I going to deploy it on the computer that I have never seen and other people are going to move it across different computers they have never seen either so this is the whole idea of you know uh portable runtime containers and devops and you know things like that however AI breaks this mode we all still remember there just one CPU the x86 CPU there's two operating systems the Windows and Linux operating systems but in today in AI we have the hardware has so you know this is the incomplete list you know there's just so many every cloud companies now have their own proprietary hardware to run AI workloads and you multiply this by a number of drivers so for instance there's CUDA different versions of CUDA Apple just announced the metal 4 which is incompatible with metal 3 on the Mac and they also have MX Right?

You know, so even on one single hardware platform, you have multiple driver software and then you have incompatible runtimes. You have PyTorch, you have lamin.cvp, you have VRM, you have SGLAN and you have all that. So for applications tha
