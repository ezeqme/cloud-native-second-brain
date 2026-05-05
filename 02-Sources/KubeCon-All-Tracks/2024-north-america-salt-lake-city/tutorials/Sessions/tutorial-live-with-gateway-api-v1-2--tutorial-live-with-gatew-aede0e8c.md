---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Tutorials"
themes: ["Networking"]
speakers: ["Flynn", "Buoyant", "Mike Morris", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1i7np/tutorial-live-with-gateway-api-v12-flynn-buoyant-mike-morris-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Live+with+Gateway+API+V1.2+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: Live with Gateway API V1.2 - Flynn, Buoyant & Mike Morris, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: Flynn, Buoyant, Mike Morris, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1i7np/tutorial-live-with-gateway-api-v12-flynn-buoyant-mike-morris-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Live+with+Gateway+API+V1.2+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: Live with Gateway API V1.2.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7np/tutorial-live-with-gateway-api-v12-flynn-buoyant-mike-morris-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Live+with+Gateway+API+V1.2+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=asbtOWQosxI
- YouTube title: Tutorial: Live with Gateway API V1.2 - Flynn, Buoyant & Mike Morris, Microsoft
- Match score: 0.74
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-live-with-gateway-api-v1-2/asbtOWQosxI.txt
- Transcript chars: 80615
- Keywords: gateway, traffic, cluster, smiley, actually, ingress, application, mesh, little, running, routing, linker, working, exactly, implementations, envoy, looking, workload

### Resumo baseado na transcript

get started I'm Flynn hi and I'm Mike and welcome to live with Gateway API 1.2 not really or um I'm in Tech evangelist for Linker I don't actually remember your title right now yeah I I'm a senior product manager uh at Microsoft working on Upstream open source things uho API and multicluster stuff as well we are also the two of the chairs for the gamma initiative within Gateway API bringing Gateway API to service mesh which is the reason why we're doing this talk yeah about massing who may be doing HDMI cable we're getting another HDMI cable this is going to be great uh yeah so uh and the cluster operators are who are doing your day-to-day kubernetes Administration they care about things like arbac they care about things like exposing Kates doio there is no service resource within that API Group the service resource exists in the the core kubernetes API Group and the official name of the core kubernetes API Group is the empty string talk to the kubernetes maintainers if you think that's we want all G API users to have is once you understand and learn the spec no matter what implementation you're working with if you change jobs if you change meshes if you change ingresses for any reason if you migrate from EO to lty if you have to work with both of them yeah yeah uh you learn this one API for the record working with both of them is way more common than you might think...

### Excerpt da transcript

get started I'm Flynn hi and I'm Mike and welcome to live with Gateway API 1.2 not really or um I'm in Tech evangelist for Linker I don't actually remember your title right now yeah I I'm a senior product manager uh at Microsoft working on Upstream open source things uho API and multicluster stuff as well we are also the two of the chairs for the gamma initiative within Gateway API bringing Gateway API to service mesh which is the reason why we're doing this talk yeah about massing service mesh we've done this talk before at ccon in Paris if you saw that one we've added a little bit but we still won't be offended if you decide to leave because it is a 90-minute workshop but we would love it if you stayed anyway um there's a little bit of an interesting thing going on here in that when we did this in Paris we had two HDMI cables and they could switch the video from laptop to laptop because my laptop is set up to run this with linkerd and Envoy Gateway and I'll be running through the same uh API same crds that we're applying to the cluster but with thiso so we're doing with one exception we're doing exactly the same configuration and two wildly different different sets of infrastructure we will tell you what the one exception is when we get to it it's a fairly minor exception um for this laptop or this Workshop we have one cable so there's going to be a certain amount of unplugging and replugging laptops we will try to keep that to a minimum yeah we'll try to keep that to a minimum because every time we do it it always has the potential to crash something so all right it's possible that we'll get to a point and just go you know what we're going to show this with just one infrastructure as we go oh and the 1.2 versus 1.1.1 thing we will also talk about a little bit but the short version is that um linkerd cannot yet use Gateway API 1.2 for very technical reasons yeah that we're working on fixing both upstream and within like a yeah exactly onward all right well let's get started so who was this for uh this talk is for platform Engineers building infrastructure for multiple application teams uh it's for application developers who want resiliency and safety with Blu green or Canary deploys and related functionality uh or anyone interested in growing their skills by learning a single API which can be used to configure dozens of different products uh the two that we're demonstrating here today are just two of I think over two dozen at least by mail Gateway API im
