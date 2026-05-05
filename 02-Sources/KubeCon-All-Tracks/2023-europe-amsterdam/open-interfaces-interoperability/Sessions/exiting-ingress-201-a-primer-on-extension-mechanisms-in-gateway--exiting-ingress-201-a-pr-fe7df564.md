---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Open Interfaces + Interoperability"
themes: ["Networking"]
speakers: ["Sunjay Bhatia", "VMware", "Inc.", "Daneyon Hansen", "Solo.io"]
sched_url: https://kccnceu2023.sched.com/event/1HyXk/exiting-ingress-201-a-primer-on-extension-mechanisms-in-gateway-api-sunjay-bhatia-vmware-inc-daneyon-hansen-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Exiting+Ingress+201%3A+A+Primer+on+Extension+Mechanisms+in+Gateway+API+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Exiting Ingress 201: A Primer on Extension Mechanisms in Gateway API - Sunjay Bhatia, VMware, Inc. & Daneyon Hansen, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sunjay Bhatia, VMware, Inc., Daneyon Hansen, Solo.io
- Schedule: https://kccnceu2023.sched.com/event/1HyXk/exiting-ingress-201-a-primer-on-extension-mechanisms-in-gateway-api-sunjay-bhatia-vmware-inc-daneyon-hansen-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Exiting+Ingress+201%3A+A+Primer+on+Extension+Mechanisms+in+Gateway+API+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Exiting Ingress 201: A Primer on Extension Mechanisms in Gateway API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXk/exiting-ingress-201-a-primer-on-extension-mechanisms-in-gateway-api-sunjay-bhatia-vmware-inc-daneyon-hansen-soloio
- YouTube search: https://www.youtube.com/results?search_query=Exiting+Ingress+201%3A+A+Primer+on+Extension+Mechanisms+in+Gateway+API+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7P55G8GsYRs
- YouTube title: Exiting Ingress 201: A Primer on Extension Mechanisms in Gateway API- Sunjay Bhatia & Daneyon Hansen
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/exiting-ingress-201-a-primer-on-extension-mechanisms-in-gateway-api/7P55G8GsYRs.txt
- Transcript chars: 25422
- Keywords: gateway, resource, reference, resources, implementation, configuration, policy, extension, within, support, custom, specific, namespace, gateways, implementations, traffic, routes, requests

### Resumo baseado na transcript

hey everyone thanks for joining us uh on a primer on Gateway API extensions my name is Damian Hansen I'm a software engineer with solo.io I've been involved with Gateway API either as a maintainer a contributor or an implementer since the Project's Inception hey everyone my name is Sanjay Bhatia I'm a software engineer at VMware and I'm a maintainer of the Contour Ingress controller and the contributor to Gateway API so what is Gateway API Gateway API is a project that's managed by the Sig Network Community within

### Excerpt da transcript

hey everyone thanks for joining us uh on a primer on Gateway API extensions my name is Damian Hansen I'm a software engineer with solo.io I've been involved with Gateway API either as a maintainer a contributor or an implementer since the Project's Inception hey everyone my name is Sanjay Bhatia I'm a software engineer at VMware and I'm a maintainer of the Contour Ingress controller and the contributor to Gateway API so what is Gateway API Gateway API is a project that's managed by the Sig Network Community within kubernetes and it is a collection of resources used to describe service routing Within kubernetes and it is a next generation of kubernetes routing and load balancing apis you may ask yourself well what's the next Generation about Gateway API Gateway API supports a ton of different protocols from grpc DLS of course HTTP layer 4 protocols the the protocol support continues to evolve within the project it can perform Advanced traffic routing this could be routing uh across different name spaces or based on information within the request if it's a header and not only the requests but also the response as well so Gateway API allows us to do a lot of really cool fun things for uh for routing traffic within kubernetes cluster or into or outside of our kubernetes cluster and I mentioned that Gateway API is a collection of resources there are some core resources that we want to talk about in more detail here there is the Gateway class resource the Gateway class resource represents a a set or a collection of gateways that have a common configuration and behavior you could think of a Gateway class uh that's called internet facing that would include all gateways that are exposed outside to the public internet while another Gateway class called internal would only be for um you know for internal communication and not exposed outside of your trust domain for example um and so beyond the Gateway class we have a Gateway this is a resource that actually is the core of Gateway API so the Gateway resources is what actually instantiates the infrastructure used um to perform these operations so typical implementations of a Gateway would be a load balancer or a proxy and when you create a gateway behind the scenes there is a controller that's responsible for watching and reconciling a Gateway that then goes ahead and um instantiates that infrastructure creates a the proxy or the load balancer maybe it creates a kubernetes service that that allows requests to the Gate
