---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Service Mesh"
themes: ["AI ML", "Networking"]
speakers: ["Kevin Leimkuhler", "Buoyant", "Doug Jordan", "Airbnb"]
sched_url: https://kccncna2022.sched.com/event/182KR/whose-packet-is-it-anyway-life-of-a-packet-through-a-service-mesh-kevin-leimkuhler-buoyant-doug-jordan-airbnb
youtube_search_url: https://www.youtube.com/results?search_query=Whose+Packet+Is+It+Anyway%3F+Life+of+a+Packet+Through+a+Service+Mesh+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Whose Packet Is It Anyway? Life of a Packet Through a Service Mesh - Kevin Leimkuhler, Buoyant & Doug Jordan, Airbnb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: United States / Detroit
- Speakers: Kevin Leimkuhler, Buoyant, Doug Jordan, Airbnb
- Schedule: https://kccncna2022.sched.com/event/182KR/whose-packet-is-it-anyway-life-of-a-packet-through-a-service-mesh-kevin-leimkuhler-buoyant-doug-jordan-airbnb
- Busca YouTube: https://www.youtube.com/results?search_query=Whose+Packet+Is+It+Anyway%3F+Life+of+a+Packet+Through+a+Service+Mesh+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Whose Packet Is It Anyway? Life of a Packet Through a Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182KR/whose-packet-is-it-anyway-life-of-a-packet-through-a-service-mesh-kevin-leimkuhler-buoyant-doug-jordan-airbnb
- YouTube search: https://www.youtube.com/results?search_query=Whose+Packet+Is+It+Anyway%3F+Life+of+a+Packet+Through+a+Service+Mesh+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TJM7juAD8B0
- YouTube title: Whose Packet Is It Anyway? Life of a Packet Through a Service Mesh - Kevin Leimkuhler & Doug Jordan
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/whose-packet-is-it-anyway-life-of-a-packet-through-a-service-mesh/TJM7juAD8B0.txt
- Transcript chars: 27728
- Keywords: container, network, mesh, traffic, containers, packet, namespace, capture, interface, address, tables, control, actually, resources, destination, packets, security, sidecar

### Resumo baseado na transcript

cool uh all right so uh Welcome to our talk everyone uh we we know it's in the uh last section of the day so we're between you and the uh Booth crawl and um yeah I don't know appreciate you everyone coming by um so yes uh welcome to whose packet Is It Anyways awesome thanks Kevin uh my name is Doug Jordan and I work at Airbnb on our istio-based service mesh called air mesh I focus on extending the mesh to Virtual Machine based workloads TCP and

### Excerpt da transcript

cool uh all right so uh Welcome to our talk everyone uh we we know it's in the uh last section of the day so we're between you and the uh Booth crawl and um yeah I don't know appreciate you everyone coming by um so yes uh welcome to whose packet Is It Anyways awesome thanks Kevin uh my name is Doug Jordan and I work at Airbnb on our istio-based service mesh called air mesh I focus on extending the mesh to Virtual Machine based workloads TCP and other Ingress use cases previously at Microsoft I worked on our bare metal control point where we adopted Linker d my handle on GitHub Twitter and other socials is usually dwj300 and as you can see from the photo on the right I enjoy cycling climbing mountains and here's a photo of me doing both those uh yeah so my name is Kevin lime cooler I am a software engineer at buoyant the creators of linker D I've been working there four years now and have worked on all the control plane components as well as the proxy uh my social handle on GitHub and Twitter is K lime cooler you can also reach me on the linkready slack for any questions you may have after the talk or in watching this recording thanks Kevin here's a quick agenda of what we'll be talking about today first Kevin will walk us through the how specifically how a TCP packet gets routed through the mesh then I'll discuss TCP debugging and walk you through a real world example breaking out TCP dump and Wireshark thank you cool uh so we'd like to start out with an overview on how a packet is routed in a service mesh so the things that we cover here will help lay the foundation for understanding some of the debugging steps Doug will take us through later I'd also like to call out that we're going to try to keep this as service mesh generic as possible while both Doug and I have had a lot of experience with sdo and Linker D the concepts we talk about today are generally shared between the two as well as some other service meshes foreign so this talk is ultimately about debugging traffic in a cluster with a service mesh so just want to make sure that we're on the same page about what a service mesh is and the common architecture of one that we or you may be debugging so mesh provides Key Properties today those tend to be the four listed here observability for things like logs and metrics routing things like traffic splitting and endpoint Discovery security think mtls and authorization policies and reliability for example transparent retries of HTTP requests circuit bre
