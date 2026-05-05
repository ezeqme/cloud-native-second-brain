---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["Security", "SRE Reliability"]
speakers: ["Dani Santos", "Michelle Mali", "Shopify"]
sched_url: https://kccnceu2025.sched.com/event/1txHC/zero-trust-at-shopify-scale-automating-mtls-across-thousands-of-services-dani-santos-michelle-mali-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Zero+Trust+at+Shopify+Scale%3A+Automating+MTLS+Across+Thousands+of+Services+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Zero Trust at Shopify Scale: Automating MTLS Across Thousands of Services - Dani Santos & Michelle Mali, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Dani Santos, Michelle Mali, Shopify
- Schedule: https://kccnceu2025.sched.com/event/1txHC/zero-trust-at-shopify-scale-automating-mtls-across-thousands-of-services-dani-santos-michelle-mali-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Zero+Trust+at+Shopify+Scale%3A+Automating+MTLS+Across+Thousands+of+Services+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Zero Trust at Shopify Scale: Automating MTLS Across Thousands of Services.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHC/zero-trust-at-shopify-scale-automating-mtls-across-thousands-of-services-dani-santos-michelle-mali-shopify
- YouTube search: https://www.youtube.com/results?search_query=Zero+Trust+at+Shopify+Scale%3A+Automating+MTLS+Across+Thousands+of+Services+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=T-nN86wTebM
- YouTube title: Zero Trust at Shopify Scale: Automating MTLS Across Thousands of Serv... Dani Santos & Michelle Mali
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/zero-trust-at-shopify-scale-automating-mtls-across-thousands-of-servic/T-nN86wTebM.txt
- Transcript chars: 33145
- Keywords: certificate, metrics, identity, spiffy, access, google, secret, shopify, authentication, certificates, search, manager, client, prometheus, security, management, rotation, infrastructure

### Resumo baseado na transcript

It's been quite the ride and we've got some fascinating insights and lessons to share. I was a contributor on the MTLS project and continue to work on securing Shopify's infrastructure. It's been around since 2009 and it centers around the belief that trusting is a vulnerability and security must be designed with the strategy never trust, always verify. Also, bring your own device policies fundamentally changed how organizations approach security with scattered workforce across various locations and devices. Relying on the traditional perimeter security model or castle emote became problematic to say the least. What are some of the challenges organizations such as Shopify face when implementing and managing them?

### Excerpt da transcript

Good morning. Today we're pulling back the curtain on Shopify's MTLS journey. It's been quite the ride and we've got some fascinating insights and lessons to share. But first, some quick introductions. I'm Michelle Mali. I've been at Shopify for nearly 5 years and joined Inf. I was a contributor on the MTLS project and continue to work on securing Shopify's infrastructure. And hey, I'm Dennis Santos. I'm a senior infosac engineer and I joined the team in Shopify back in 2020. My recent projects involve increasing the adoption of MTLS for internal service authentication and using attested identities for ACL. Here's what we're going to be covering today. Uh we're going to start with a brief refresher on zero trust and then we move on to talk about workload identity and adopting spiffy. Then we cover some options for service to service authentication. We also talk about how we do certificate management observ observability and we finish with a demo followed by key takeaways. We're going to be showing snippets of the demo throughout the slides but we will have a final session with a video showing all the pieces together.

But first things first, why does zero trust matter? Zero trust is a concept founded by this fine gentleman, John Kindervag. It's been around since 2009 and it centers around the belief that trusting is a vulnerability and security must be designed with the strategy never trust, always verify. We have seen a growing push for the zero trust model across companies and government agencies. The latest technology trends for 2025 published by O'Reilly states that there was a 13% rise in interest in the topic. Now let's take a step back and try to understand why this is the case. Oops. You remember in 2020 we had the pandemic and it triggered an unprecedented shift in how organizations operate and this global crisis accelerated the consumption of toilet paper and also accelerated the adoption of cloud infrastructure as companies rapidly adapted to support remote work and digital operations. Also, bring your own device policies fundamentally changed how organizations approach security with scattered workforce across various locations and devices.

Relying on the traditional perimeter security model or castle emote became problematic to say the least. Um, in zero trust we always verify the identity of every entity requesting access both human and non-human. Non-human entities like VMs, containers, applications and services are called workloads. This ve
