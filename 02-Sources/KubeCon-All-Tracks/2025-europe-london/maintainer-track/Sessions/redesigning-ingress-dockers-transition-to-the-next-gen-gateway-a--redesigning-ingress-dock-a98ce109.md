---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Kateryna Nezdolii", "Ryan Hristovski", "Docker"]
sched_url: https://kccnceu2025.sched.com/event/1tcza/redesigning-ingress-dockers-transition-to-the-next-gen-gateway-api-kateryna-nezdolii-ryan-hristovski-docker
youtube_search_url: https://www.youtube.com/results?search_query=Redesigning+Ingress%3A+Docker%E2%80%99s+Transition+To+the+Next-Gen+Gateway+API+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Redesigning Ingress: Docker’s Transition To the Next-Gen Gateway API - Kateryna Nezdolii & Ryan Hristovski, Docker

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Kateryna Nezdolii, Ryan Hristovski, Docker
- Schedule: https://kccnceu2025.sched.com/event/1tcza/redesigning-ingress-dockers-transition-to-the-next-gen-gateway-api-kateryna-nezdolii-ryan-hristovski-docker
- Busca YouTube: https://www.youtube.com/results?search_query=Redesigning+Ingress%3A+Docker%E2%80%99s+Transition+To+the+Next-Gen+Gateway+API+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Redesigning Ingress: Docker’s Transition To the Next-Gen Gateway API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcza/redesigning-ingress-dockers-transition-to-the-next-gen-gateway-api-kateryna-nezdolii-ryan-hristovski-docker
- YouTube search: https://www.youtube.com/results?search_query=Redesigning+Ingress%3A+Docker%E2%80%99s+Transition+To+the+Next-Gen+Gateway+API+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ea5OuNjpi9M
- YouTube title: Redesigning Ingress: Docker’s Transition To the Next-Gen Gate... Kateryna Nezdolii & Ryan Hristovski
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/redesigning-ingress-dockers-transition-to-the-next-gen-gateway-api/Ea5OuNjpi9M.txt
- Transcript chars: 27095
- Keywords: envoy, gateway, traffic, configuration, docker, migration, routing, canary, ingress, control, haroxy, features, request, feature, internal, filter, policy, balancer

### Resumo baseado na transcript

Hi everyone, my name is Katina Onesik and I currently work as a SRA docker and also a maintainer of envoy proxy project. Uh very excited to attend CubeCon this year here in London and share our migration journey with you. This led us to look for a solution that could solve this problem without all the extra services and sidecars that we needed to maintain. Lastly, Hgroxy does not natively support open telemetry, which is what all services at Docker are using for our tracing. We narrowed our proxy selection to envoy and traffic with traffic offering simpler runtime updates and golink based extensibility but falling behind envoy and high load performance and advanced native features. It has a steeper learning curve, but our ability to contribute upstream upstream thanks to uh Katarina as an envoy maintainer gave us confidence to move forward.

### Excerpt da transcript

Hi everyone, my name is Katina Onesik and I currently work as a SRA docker and also a maintainer of envoy proxy project. Uh very excited to attend CubeCon this year here in London and share our migration journey with you. I'm here today virtually with Ryan. Hello everyone. I'm Ryan and I'm an infrastructure engineer at Docker and I'm also really excited to be here with you at CubeCon virtually. I wish I could have made it in person but I'm tuning in for my honeymoon. Today we're going to share how Docker redesigned its ingress system and made the leap from our legacy standalone harroxy and engineext stack to a modern envoy gateway solution. We're going to dive right in. Here we have a simplified overview of our legacy ingress stack. The typical Docker Hub request follows this pattern. The client's request will go through the external AWS network load balancer which then arrives at our haroxy. external haroxy. Haroxy will determine here if there are any abuse rate limits that are being hit. If not, it's going to send the request to engine X.

Once it sets EngineX, it's going to validate JWT tokens with Louisis scripts. It's going to check Reddus for session revocation and it's going to forward authenticated requests to the internal network load balancer and internal haroxy. From here, it's going to load balance the request to the expected back end. Now, this system has served us well over the years. Uh, but I'm going to be covering three core components that make the legacy stack unique and create major pain points at Docker. I'll be reviewing the legacy console reliance, engine X, and sidecar blowup. Now, I know this diagram is a lot to digest and you don't need to fully understand it. We just wanted to highlight the complexity of our previous consensus protocol-based systems where we heavily relied on console clients and servers for key value store, dynamic reconfiguration and even in some cases service discovery. Running the console server and client had introduced another critical component that must remain highly available for our ingress systems to function.

This made our systems a lot more fragile if console ever experienced downtime or networking issues. This led us to look for a solution that could solve this problem without all the extra services and sidecars that we needed to maintain. Engine X became a painoint because it was introduced nearly 10 years ago to handle requirements haroxy couldn't fulfill at the time. This is also handled by an ex
