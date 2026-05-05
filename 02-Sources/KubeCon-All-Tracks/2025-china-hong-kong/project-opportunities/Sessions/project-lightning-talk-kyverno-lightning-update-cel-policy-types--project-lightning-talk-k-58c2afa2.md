---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Project Opportunities"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Shuting Zhao", "Maintainer"]
sched_url: https://kccncchn2025.sched.com/event/1xjzQ/project-lightning-talk-kyverno-lightning-update-cel-policy-types-in-action-shuting-zhao-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kyverno+Lightning+Update%3A+CEL+%26+Policy+Types+in+Action+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Kyverno Lightning Update: CEL & Policy Types in Action - Shuting Zhao, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: China / Hong Kong
- Speakers: Shuting Zhao, Maintainer
- Schedule: https://kccncchn2025.sched.com/event/1xjzQ/project-lightning-talk-kyverno-lightning-update-cel-policy-types-in-action-shuting-zhao-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kyverno+Lightning+Update%3A+CEL+%26+Policy+Types+in+Action+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Kyverno Lightning Update: CEL & Policy Types in Action.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1xjzQ/project-lightning-talk-kyverno-lightning-update-cel-policy-types-in-action-shuting-zhao-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kyverno+Lightning+Update%3A+CEL+%26+Policy+Types+in+Action+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YTR1JYhv3sQ
- YouTube title: Project Lightning Talk: Kyverno Lightning Update: CEL & Policy Types in Action - Shuting Zhao
- Match score: 0.999
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-kyverno-lightning-update-cel-policy-types-in-ac/YTR1JYhv3sQ.txt
- Transcript chars: 4847
- Keywords: policy, validating, policies, kivero, emission, lightning, management, reporting, across, engine, expression, controllers, action, provide, kverno, shouldn, needed, admission

### Resumo baseado na transcript

I'm super excited to be here to provide a lightning talk uh for Kivero updates. But first of all, let's step back and take a look at where we are right now. And when Kubernetes announced that the validating emission policy going to build on top of common expression language which is cell, it was clear that cell will become the standard of policy expressions across your entire CNCF ecosystem. And you know that is it still uses cell gateway API uses cell and now Kubernetes uses cell. It's not just an add-on but as our foundation and with that you're able to learn one expression language that applies everywhere across your cloud native stack and secondly um the complete Kubernetes work policy coverage became essential. last four years into a unified architecture with um consistent APIs and integrated to gen.

### Excerpt da transcript

Great. Um hello everyone. I'm super excited to be here to provide a lightning talk uh for Kivero updates. So um before we dive into details, a quick introduction of myself. I'm shooting Zhao a kerno montenna from Namada. And today we're going to talk about what's new in Kverno. But first of all, let's step back and take a look at where we are right now. Right. So uh we launched a covero about four years ago and um one of the or some of the core principles that we followed while building the project um first of all we always want to simplify Kubernetes operations. So writing policies and managing policies shouldn't really require a PhD in CS right. So um the platform teams needed something that natural um within their existing Kubernetes workflow and then um it should address all aspects of policy management not just admission controls. So a real world policy needs a full life cycle policy management including reporting the testing ability the global exceptions and so on. And this approach worked right.

We've seen tons of organizations adopted Civero because it solved real problems. And then later on we realized that something bigger. Um the same reason for the need of simple comprehensive and optimized policy management are needed should exist everywhere and across your um like infrastructures and kivero shouldn't just you know be the kivero policy engine only. So we have extended it to a generalpurpose policy engine which allows you to apply caberno policies anywhere to any uh structured data. And you may ask why change right? This answer is very simple. As Kubernetes has evolved we want to stay true to our to our mission. And when Kubernetes announced that the validating emission policy going to build on top of common expression language which is cell, it was clear that cell will become the standard of policy expressions across your entire CNCF ecosystem. And you know that is it still uses cell gateway API uses cell and now Kubernetes uses cell. So we have bu the cell powered policy engine. um framework and cover.

It's not just an add-on but as our foundation and with that you're able to learn one expression language that applies everywhere across your cloud native stack and secondly um the complete Kubernetes work policy coverage became essential. A recent talk uh from Kubuaniu um delivered by the policy working group suggested that you should use beatin policy types for baseline and consider admission web hooks or the controllers for more advanced sc
