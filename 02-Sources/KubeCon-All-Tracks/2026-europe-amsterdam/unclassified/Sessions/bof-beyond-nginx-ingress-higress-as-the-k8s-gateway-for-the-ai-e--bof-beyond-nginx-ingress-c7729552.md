---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Unclassified"
themes: ["AI ML", "Networking"]
speakers: []
sched_url: https://kccnceu2026.sched.com/event/2GgLh/bof-beyond-nginx-ingress-higress-as-the-k8s-gateway-for-the-ai-era
youtube_search_url: https://www.youtube.com/results?search_query=BoF+%7C+Beyond+Nginx+Ingress%3A+Higress+as+the+K8s+Gateway+for+the+AI+Era+CNCF+KubeCon+2026
slides: []
status: parsed
---

# BoF | Beyond Nginx Ingress: Higress as the K8s Gateway for the AI Era

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: N/A
- Schedule: https://kccnceu2026.sched.com/event/2GgLh/bof-beyond-nginx-ingress-higress-as-the-k8s-gateway-for-the-ai-era
- Busca YouTube: https://www.youtube.com/results?search_query=BoF+%7C+Beyond+Nginx+Ingress%3A+Higress+as+the+K8s+Gateway+for+the+AI+Era+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre BoF | Beyond Nginx Ingress: Higress as the K8s Gateway for the AI Era.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2GgLh/bof-beyond-nginx-ingress-higress-as-the-k8s-gateway-for-the-ai-era
- YouTube search: https://www.youtube.com/results?search_query=BoF+%7C+Beyond+Nginx+Ingress%3A+Higress+as+the+K8s+Gateway+for+the+AI+Era+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FURcBVNuK0U
- YouTube title: BoF | Beyond Nginx Ingress: Higress as the K8s Gateway for the AI Era
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/bof-beyond-nginx-ingress-higress-as-the-k8s-gateway-for-the-ai-era/FURcBVNuK0U.txt
- Transcript chars: 17934
- Keywords: gateway, support, ingress, features, issues, highress, plugins, traffic, automatically, envoy, engine, write, request, higress, migrate, provide, annotations, feature

### Resumo baseado na transcript

Uh thank you for also being here and uh I'm from Alibaba cloud and uh today I'm gonna talk about the beyond in ingress hyres as the kubernetes gateway for the AI era. Uh just a quick note that the hyres just joins the CNCF sandbox a couple of days before writing the keynote has it has been announced. So we actually we are using at Alibaba column we using used the engine based ingress before and we have faced several challenges. Uh engine has uh designed for the shortlived connections and the for the uh long live multiplex especially multiplex uh http2 connections we suffer from um uneven load balancing issues. So that will um will not be a a good practice when we are scaling to thousands of uh maybe tens of thousands of configurations in one single kubernetes cluster. So I'll briefly introduce the brief big milestones before the hyres has been open sourced and the so we are we we decide to uh embrace the and envoy uh architecture.

### Excerpt da transcript

My name is Hushing. Uh thank you for also being here and uh I'm from Alibaba cloud and uh today I'm gonna talk about the beyond in ingress hyres as the kubernetes gateway for the AI era. Uh just a quick note that the hyres just joins the CNCF sandbox a couple of days before writing the keynote has it has been announced. So it's a new project in CSF sandbox. Okay, let's let me first uh talk about the retirement of engines in ingress. So this is a very special moment that the you know all know that kubernetes the s network and security response community has announced that the retirement of engine ingress. uh so right at the end of this months it will be uh retired and uh so that means a couple of days later we will get no further release no bug fix or security patches. So this is the fact but another fact is that there according to an estimation that 50% of the global cloud native uh environment still use engines uh some sort of engines infrastructure ingress infrastructure. So this is a crucial uh uh issue for us.

We need to address that. And then there's another uh uh critical issue that this engines allows us to write uh allocation based code snippets which allows to write uh any form of um engines config. Uh this is very flexible and powerful but uh since the retirement there were going to be very critical issues critical vulnerabilities. So that's one thing we need to address. So we actually we are using at Alibaba column we using used the engine based ingress before and we have faced several challenges. I I'll list some of them. The first one is the traffic jitter for long lived connections. So as you will know that when we are updating engine synress the config uh every config will go through a new uh worker process to uh update the config but so this which will cause the longlived connection like gRPC web socket to terminate the connect connections and reestablished so this uh is very uh painful for our users. So they were got suffered from the uh this kind of uh update issues. So another uh issue is the JRPC load balancing issues.

Uh engine has uh designed for the shortlived connections and the for the uh long live multiplex especially multiplex uh http2 connections we suffer from um uneven load balancing issues. So even enginex has provides support for the GPC load balancing. But if we are using a non connection and send request multiple uh multiplexing request over one single connections it will uh cause some um load balancing issues and resour
