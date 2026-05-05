---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Ariel Septon", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcvK/project-lightning-talk-expanding-crossplanes-reach-providers-bridges-and-extensibility-ariel-septon-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Expanding+Crossplane%E2%80%99s+Reach+-+Providers%2C+Bridges%2C+and+Extensibility+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Expanding Crossplane’s Reach - Providers, Bridges, and Extensibility - Ariel Septon, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Ariel Septon, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcvK/project-lightning-talk-expanding-crossplanes-reach-providers-bridges-and-extensibility-ariel-septon-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Expanding+Crossplane%E2%80%99s+Reach+-+Providers%2C+Bridges%2C+and+Extensibility+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Expanding Crossplane’s Reach - Providers, Bridges, and Extensibility.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvK/project-lightning-talk-expanding-crossplanes-reach-providers-bridges-and-extensibility-ariel-septon-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Expanding+Crossplane%E2%80%99s+Reach+-+Providers%2C+Bridges%2C+and+Extensibility+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8-ovtwX2l7k
- YouTube title: Project Lightning Talk: Expanding Crossplane’s Reach - Providers, Bridges, and Exten... Ariel Septon
- Match score: 0.984
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-expanding-crossplanes-reach-providers-bridges-a/8-ovtwX2l7k.txt
- Transcript chars: 4096
- Keywords: crossplane, infrastructure, internal, manage, provider, resources, management, everything, manual, provide, providers, working, managed, critical, existing, database, provisioning, making

### Resumo baseado na transcript

Hi, my name is Ariel and a few years ago I was working at a company with a large complex infrastructure. We used crossplane and Argo CD as our control plane and infrastructure as code tools. Even worse, no versioning, no audit logs, no history, no way to track or understand the current state of resources. There's no automation, so you can't track drift or enforce changes, and it just doesn't scale. I designed it to let users define API calls as crossplane managed resources, making it possible to manage any API. For teams that need even more flexibility, crossplane also provides provided Kubernetes and function Go templating.

### Excerpt da transcript

Hi, my name is Ariel and a few years ago I was working at a company with a large complex infrastructure. We used crossplane and Argo CD as our control plane and infrastructure as code tools. But not everything could be managed through them. Some of our most critical systems were internal and had no existing provider. One of them was our internal database provisioning system. It had an API but no provider just raw HTTP endpoint. So what do you do when the provider you need doesn't exist? Abandon crossplane altogether spend weeks writing a brand new provider from scratch or go back to manual work. We kept working around it but it didn't scale and it didn't fit into our infrastructure as code workflows. Infrastructure as code has transformed the way we manage infrastructure. Instead of manual provisioning, resources are now created and updated declaratively, making everything more consistent, reusable, and scalable. But while we've solved this problem for most technologies, internal services remain a major blind spot.

The issue is not unique to databases. Many companies rely heavily on their own custom internal services. We're talking about things like secrets management, feature flag management, quota management, all critical, non-standardized. Unmanaged services become a major challenge. Even when we try to do something as simple as a version update without infrastructure as code management, we have to trigger API calls manually, hope no databases are missed, and coordinate across teams because no one has clear visibility into database ownership. Even worse, no versioning, no audit logs, no history, no way to track or understand the current state of resources. There is no standardization and no guarantee that this change is applied everywhere. And without declarative management, we fall back to manual work interacting with internal APIs by hand. It might start small, but it quickly spirals into an unscalable mess. This creates se the team some tries to keep track in spreadsheets. things like how many instances exist, where they're deployed, who owns them.

This creates several issues. The data is often out of date. There's no automation, so you can't track drift or enforce changes, and it just doesn't scale. The more services you have, the harder it is to manage or trust any of it. We've been already using infrastructure as code to manage everything else. So, how do we bring that same consistency to internal services? When I looked at existing infrastructu
