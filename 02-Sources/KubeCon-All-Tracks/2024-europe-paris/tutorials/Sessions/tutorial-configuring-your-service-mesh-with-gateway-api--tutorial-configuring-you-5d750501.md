---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Tutorials"
themes: ["Networking"]
speakers: ["Mike Morris", "Microsoft", "Flynn", "Buoyant"]
sched_url: https://kccnceu2024.sched.com/event/1YeOL/tutorial-configuring-your-service-mesh-with-gateway-api-mike-morris-microsoft-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Configuring+Your+Service+Mesh+with+Gateway+API+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: Configuring Your Service Mesh with Gateway API - Mike Morris, Microsoft & Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Tutorials]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Mike Morris, Microsoft, Flynn, Buoyant
- Schedule: https://kccnceu2024.sched.com/event/1YeOL/tutorial-configuring-your-service-mesh-with-gateway-api-mike-morris-microsoft-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Configuring+Your+Service+Mesh+with+Gateway+API+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: Configuring Your Service Mesh with Gateway API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOL/tutorial-configuring-your-service-mesh-with-gateway-api-mike-morris-microsoft-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Configuring+Your+Service+Mesh+with+Gateway+API+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UMGRp0fGk3o
- YouTube title: Tutorial: Configuring Your Service Mesh with Gateway API - Mike Morris, Microsoft & Flynn, Buoyant
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-configuring-your-service-mesh-with-gateway-api/UMGRp0fGk3o.txt
- Transcript chars: 73133
- Keywords: gateway, actually, traffic, mesh, ingress, cluster, workload, controller, smiley, little, linkerd, resource, laptop, application, linker, working, switch, version

### Resumo baseado na transcript

so welcome to the Gateway API Workshop I'm Flynn and this is Mike I'm Mike I am a tech evangelist with buyant I work primarily with Linker in a past life I was also the original author of The Emissary Ingress API Gateway and these days I work also with Gateway API and I'm a co-lead for the gamma initiative over to Mike uh I'm a product manager at Microsoft now uh I'm currently working on our Upstream Open Source service mesh team uh with uh ISO and Gateway API inside the cluster this is the Engish problem you have to have a way to let people use the things inside your cluster or what's the point this is the first problem you're going to have to solve with Cloud native always so we tend

### Excerpt da transcript

so welcome to the Gateway API Workshop I'm Flynn and this is Mike I'm Mike I am a tech evangelist with buyant I work primarily with Linker in a past life I was also the original author of The Emissary Ingress API Gateway and these days I work also with Gateway API and I'm a co-lead for the gamma initiative over to Mike uh I'm a product manager at Microsoft now uh I'm currently working on our Upstream Open Source service mesh team uh with uh ISO and Gateway API I've been involved with the Gateway API project for over two years now and prior to that I was uh at hash cor working on Console service mesh so been around the service mesh space for quite a bit and you also used to be a co-lead of gamma yes yeah I I was one of the founding co-leads of gamma along with uh John Howard from Google and Keith madx from Microsoft so what this means is that you have a couple of people up here who now work in marketing and management trying to talk to you about technical things wish luck um I should also apologize in advance if you see me making weird winsing faces or something it's because I broke this color bone a week and a half ago it's not a commentary on Gateway API or because we broke our demo well we might have broken the demo anyway I mean we'll find out um we also we haven't really gone through and done a lot of workshops in this format before so on the one hand I don't actually know if it's going to take an hour and a half to get through everything uh but you know feel free to ask questions and I believe there are a couple of microphones out of the audience if you want to or just you know yell out and we'll try to help people out um and if we finish early then we finish early and that'll be great because that will mean that everything went swimmingly and it's really easy to use so who are we here for yeah we're here for platform Engineers application developers infrastructure people uh really anybody who's trying to work with applications in kubernetes if you are doing applications in kubernetes you will always have to solve problems that Gateway API is here to solve if you are doing kubernetes and you're not doing it for the purpose of applications then I'm not sure what you're doing exactly because nobody runs clusters just to say they're running the cluster everybody's trying to do something with a cluster so that's what we're here to talk about and and one of the strengths of Gateway API is really um that it's also for platform Engineers too so even if you'r
