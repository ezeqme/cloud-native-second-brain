---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Oskar Kristiansen", "Saxo Bank"]
sched_url: https://kccnceu2026.sched.com/event/2CW3e/inside-saxo-service-blueprint-implementing-kubernetes-operators-for-legacy-enterprise-infrastructure-oskar-kristiansen-saxo-bank
youtube_search_url: https://www.youtube.com/results?search_query=Inside+Saxo+Service+Blueprint%3A+Implementing+Kubernetes+Operators+for+Legacy+Enterprise+Infrastructure+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Inside Saxo Service Blueprint: Implementing Kubernetes Operators for Legacy Enterprise Infrastructure - Oskar Kristiansen, Saxo Bank

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Oskar Kristiansen, Saxo Bank
- Schedule: https://kccnceu2026.sched.com/event/2CW3e/inside-saxo-service-blueprint-implementing-kubernetes-operators-for-legacy-enterprise-infrastructure-oskar-kristiansen-saxo-bank
- Busca YouTube: https://www.youtube.com/results?search_query=Inside+Saxo+Service+Blueprint%3A+Implementing+Kubernetes+Operators+for+Legacy+Enterprise+Infrastructure+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Inside Saxo Service Blueprint: Implementing Kubernetes Operators for Legacy Enterprise Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3e/inside-saxo-service-blueprint-implementing-kubernetes-operators-for-legacy-enterprise-infrastructure-oskar-kristiansen-saxo-bank
- YouTube search: https://www.youtube.com/results?search_query=Inside+Saxo+Service+Blueprint%3A+Implementing+Kubernetes+Operators+for+Legacy+Enterprise+Infrastructure+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D6c5lsOz38U
- YouTube title: Inside Saxo Service Blueprint: Implementing Kubernetes Operators for Legacy Ent... Oskar Kristiansen
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/inside-saxo-service-blueprint-implementing-kubernetes-operators-for-le/D6c5lsOz38U.txt
- Transcript chars: 24805
- Keywords: infrastructure, identity, actually, namespace, account, access, operator, blueprint, everything, catalog, operators, provisioning, managed, repository, status, resources, platform, running

### Resumo baseado na transcript

Today, I want to speak about the Saxo service blueprint, uh which is what me and my team has been working on for the last 3 years. And it's to use Kubernetes operators and GitOps to modernize and automate the infrastructure and IAM provisioning within Saxo Bank. Uh so, now I can tell you about the engineering problem that we had to solve. The cost and risk of refactoring them to run in containers is simply not justified. Some workloads use IP multicast, which our current Kubernetes network setup doesn't make straightforward to implement. Uh we have cloud-native workloads on Kubernetes, but we also have traditional workloads on servers that are not going anywhere anytime soon.

### Excerpt da transcript

Today, I want to speak about the Saxo service blueprint, uh which is what me and my team has been working on for the last 3 years. And it's to use Kubernetes operators and GitOps to modernize and automate the infrastructure and IAM provisioning within Saxo Bank. My name is Oscar Christensen, and I'm a senior enterprise platform engineer at Saxo. So, to begin, I will quickly present Saxo Bank so we have a context for why this system is beneficial and what led us to take some of the decisions that we did. Saxo Bank was founded in 1992. It's denoted as a systemically important financial institution in Denmark. It manages 118 billion euros in client assets and is spread across which is spread across 1.4 million end clients. And uh we work across 12 offices, which together contains 2,432 employees. We have both direct consumer-facing products for investors of different levels as well as partner integrations and APIs. And uh Saxo Bank operates across the world with spread-out offices, institutional clients, and direct clients as well.

Financial instruments can be traded through Saxo includes everything from currencies, bonds, mutual funds, margin lending, even crypto. And uh in total, it's more than 71,000 different ones. So, all of this is just to say that the product offered by Saxo is very complex, and it's under heavy compliance and regulatory demands. And as a more than 30-year-old fintech company and bank, it includes an enormous amount of more or less legacy applications and infrastructure, which must be kept running and compliant. So, that's the business. Uh so, now I can tell you about the engineering problem that we had to solve. Uh first, we'll look at the old way of provisioning infrastructure in Saxo. Uh a developer has built some new service, and it works, and it fits the requirements, and the test passes, and everything. But before it runs, of course, it can run it, of course, it needs a few things. Needs a server to run on. It needs firewall rules so traffic can reach it. It needs a service account so it can authenticate to internal systems.

It needs a role grant on an SQL database. And it needs DNS and uh TLS certificate so other services can call it and verify against it. So, for this, uh this is like the bare minimum to get some service running in production. And that's already six things across five different infrastructure teams. So, the old way, they would open six tickets or send send off six emails. And then they would wait because each
