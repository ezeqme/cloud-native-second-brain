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
themes: ["Networking"]
speakers: ["Kalen Wessel", "Zapier"]
sched_url: https://kccnceu2026.sched.com/event/2EFzm/cloud-native-theater-envoycon-from-ingress-nginx-to-envoy-gateway-at-zapier-the-benefits-challenges-and-migration-lessons-that-matter-kalen-wessel-zapier
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+From+ingress-nginx+to+Envoy+Gateway+at+Zapier%3A+The+Benefits%2C+Challenges%2C+and+Migration+Lessons+That+Matter+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | EnvoyCon: From ingress-nginx to Envoy Gateway at Zapier: The Benefits, Challenges, and Migration Lessons That Matter - Kalen Wessel, Zapier

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kalen Wessel, Zapier
- Schedule: https://kccnceu2026.sched.com/event/2EFzm/cloud-native-theater-envoycon-from-ingress-nginx-to-envoy-gateway-at-zapier-the-benefits-challenges-and-migration-lessons-that-matter-kalen-wessel-zapier
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+From+ingress-nginx+to+Envoy+Gateway+at+Zapier%3A+The+Benefits%2C+Challenges%2C+and+Migration+Lessons+That+Matter+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | EnvoyCon: From ingress-nginx to Envoy Gateway at Zapier: The Benefits, Challenges, and Migration Lessons That Matter.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFzm/cloud-native-theater-envoycon-from-ingress-nginx-to-envoy-gateway-at-zapier-the-benefits-challenges-and-migration-lessons-that-matter-kalen-wessel-zapier
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+From+ingress-nginx+to+Envoy+Gateway+at+Zapier%3A+The+Benefits%2C+Challenges%2C+and+Migration+Lessons+That+Matter+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kIj2U13VZJY
- YouTube title: Cloud Native Theater | EnvoyCon: From ingress-nginx to Envoy Gateway at Zapier: The... Kalen Wessel
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-envoycon-from-ingress-nginx-to-envoy-gateway-at-z/kIj2U13VZJY.txt
- Transcript chars: 13813
- Keywords: envoy, gateway, ingress, traffic, migration, policy, request, started, baselines, enginex, simply, buffer, engine, annotations, production, application, backend, latency

### Resumo baseado na transcript

Hi everyone, my name is Kayn Wessle and I'm a senior site reliability engineer at Zapier. Today I'm going to be walking you through our migration from Ingress Engine X to Envoy Gateway. At this point we were sold on Kubernetes API gateway uh but which implementation did we want to go with? Finding those sharp edges up front uh directly informed our design decisions and made the rest of the roll out much smoother. For example, adding header based canary support to our monolith uh deployment demonstrated early uh value and uh it strengthened our testing strategy. At each step we compared those envoy metrics against the engineext baselines I was telling you about earlier.

### Excerpt da transcript

Hi everyone, my name is Kayn Wessle and I'm a senior site reliability engineer at Zapier. Today I'm going to be walking you through our migration from Ingress Engine X to Envoy Gateway. I'll touch on why we made the move, how we approached it, some of the unexpected issues we ran into, and the new features we're capitalizing on. So why we need to move? Well, for starters, the writing was on the wall. I'm sure the EngineX end of life announcement is why many of you are here in the audience today. Along with the ingress API being marked as frozen for quite some time and the gateway API gaining traction, ingress's days just felt numbered. But not only that, years of tech debt. Like many companies, we didn't wake up and choose chaos. We accumulated it. Over the years, we had built up a collection of differing load balances. uh various ingress ingress enginex controllers annotations started to vary by teams environments behaved inconsistently staging and production slowly diverged. This naturally created pain points.

The fragmentation introduced drift which occasionally even resulted in the odd outage. And sure, we could have simply migrated to a different ingress controller, but this felt like the right opportunity uh and right moment to rebuild the ingress layer the way we always wanted it. And this time with the Kubernetes API gateway at the center. So what do we all get with the Kubernetes API gateway? Well, for starters, a clear separation of responsibilities. Platform teams manage their gateways and gateway classes. application teams handle their HP routes and backend traffic policies. Strongly typed CRDs uh now let us finally drop those delicate annotation strings which I'm sure have all bit us one time or another. And with proper schemas in place, CI linting can catch those silly syntax errors a lot earlier. Gateway API also gives us richer tech primitives uh sorry traffic primitives out of the box. uh traffic splitting, headerbased canary matching and more and all again without relying on those controller specific annotations.

At this point we were sold on Kubernetes API gateway uh but which implementation did we want to go with? Last March we evaluated uh multiple implementations such as stto glue and a few others. Envoy gateway uh stood out as the winner for us when compared to other options. its Kubernetes API alignment uh was the strongest. You have to remember this was already a year ago, so I'm sure some of the others are catching up. It also p
