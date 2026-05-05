---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["AI ML", "Networking"]
speakers: ["Xiaolin Lin", "Bloomberg"]
sched_url: https://kccnceu2026.sched.com/event/2EFzj/cloud-native-theater-envoycon-the-future-of-ai-traffic-whats-new-in-envoy-ai-gateway-2026-xiaolin-lin-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+The+Future+of+AI+Traffic%3A+What%27s+New+in+Envoy+AI+Gateway+2026+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | EnvoyCon: The Future of AI Traffic: What's New in Envoy AI Gateway 2026 - Xiaolin Lin, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Xiaolin Lin, Bloomberg
- Schedule: https://kccnceu2026.sched.com/event/2EFzj/cloud-native-theater-envoycon-the-future-of-ai-traffic-whats-new-in-envoy-ai-gateway-2026-xiaolin-lin-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+The+Future+of+AI+Traffic%3A+What%27s+New+in+Envoy+AI+Gateway+2026+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | EnvoyCon: The Future of AI Traffic: What's New in Envoy AI Gateway 2026.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFzj/cloud-native-theater-envoycon-the-future-of-ai-traffic-whats-new-in-envoy-ai-gateway-2026-xiaolin-lin-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+The+Future+of+AI+Traffic%3A+What%27s+New+in+Envoy+AI+Gateway+2026+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7OkSrMBirmc
- YouTube title: Cloud Native Theater | EnvoyCon: The Future of AI Traffic: What's New in Envoy AI Tra... Xiaolin Lin
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-envoycon-the-future-of-ai-traffic-whats-new-in-en/7OkSrMBirmc.txt
- Transcript chars: 15678
- Keywords: gateway, provider, specific, traffic, response, client, cost, routing, request, envoy, processing, looking, handle, little, controller, format, depends, offering

### Resumo baseado na transcript

Um so I'm going to talk about what's the future look like of AI traffic. So before I get into there, so I want to highlight what kind of problem we trying to solve uh with this on AI gateway. to share that the reliability uh as well as like end to end security like authentications authorizations uh etc. Uh and uh early this year uh well now uh the main uh the thing is that we focus on the cost managements. Those are the uh kind of a pillars to help you to uh further optimize your cost and then be efficiency. uh and tracing the spans and through the uh streaming and non-streaming case because like uh streaming case you want to look into like intra token latency to improve your uh user experience and uh and then non-streaming cases is more kind of you can think about like traditional request and response path.

### Excerpt da transcript

Good afternoon everyone. Thank you for joining the talk. Uh my name is Shins for Boomber. Uh we are the I'm from the AI traffic team at Boomber. We manage all the infants. Uh and then the GI traffic at Boomer. Um so I'm going to talk about what's the future look like of AI traffic. Uh what's the news coming out in the on AI gateway. So before I get into there, so I want to highlight what kind of problem we trying to solve uh with this on AI gateway. uh previous two talk speakers talk about the onoy envoy gateway. So we pretty much kind of on top of that and to dealing with the AI uh specific uh processing. So uh I want to highlight that the traditional AI API gateways for sure because that the error traffic requires special handling like you extract the model names from the uh payload instead of like looking at a header and also organizations looking to like uh control the cost uh about the token usage. Uh and also like sometimes the model fade over uh doesn't work that way because like the a lot of model is not like cloud provider have their issues and then we also you in order to provide the enterprise grade we need to do a lot of um fail over and then smart failover as well.

Um and also um as I mentioned that we need to have like multi-provider integration. Uh different provider have their own specific API uh the way to authenticate and then the way to handle the uh specific of the the traffic as well. Uh like also the capacity type. Um and the other uh challenge or objective is that we want to make that uh operational uh easy for the platform owners and also building the uh governance into that to monitor this observability and token usage cost uh as well and uh the other part is that um when we building the onway AI gateway we try to look out outside is there existing solutions that is open and collaborate we didn't realize there's a one and then we start to talking with the uh on community and then we start building this uh gateway uh with the different company and different developer and contributors from all over the world. Um uh so on gateway is essentially is a uh a project on built on top of and on gateway uh from to handling the AI specific uh workloads.

So the key object uh I think I'm kind of a luing into the array uh we try to provide a unifi uh API layer uh to for routing and manage the uh error and AI traffic and also supporting the uh automatic failover mechanism to share that the reliability uh as well as like end to end security like
