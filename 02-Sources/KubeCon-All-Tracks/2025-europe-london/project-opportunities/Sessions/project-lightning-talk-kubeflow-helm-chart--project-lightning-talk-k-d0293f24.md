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
speakers: ["Krzysztof Romanowski", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcvo/project-lightning-talk-kubeflow-helm-chart-krzysztof-romanowski-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubeflow+Helm+Chart+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Kubeflow Helm Chart - Krzysztof Romanowski, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Krzysztof Romanowski, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcvo/project-lightning-talk-kubeflow-helm-chart-krzysztof-romanowski-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubeflow+Helm+Chart+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Kubeflow Helm Chart.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvo/project-lightning-talk-kubeflow-helm-chart-krzysztof-romanowski-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubeflow+Helm+Chart+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NkOV4_JV4t4
- YouTube title: Project Lightning Talk: Kubeflow Helm Chart - Krzysztof Romanowski, Maintainer
- Match score: 0.804
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-kubeflow-helm-chart/NkOV4_JV4t4.txt
- Transcript chars: 4788
- Keywords: cubeflow, components, customize, projects, infrastructure, everything, bigger, integrate, repository, leading, around, helmchart, parameterize, environments, inside, company, parameterization, whatever

### Resumo baseado na transcript

And um I want to present something that I was leading around cubeflow specifically for Helmchart. So this is not a presentation about CubeFlow about this work around Helmchart.

### Excerpt da transcript

My name is Christopher Manovski. Don't tangle your tongue. Just call me Raman. I'm lead Kubernetes engineer at Raj. And um I want to present something that I was leading around cubeflow specifically for Helmchart. So this is not a presentation about CubeFlow about this work around Helmchart. And uh some of you that know cubeflow a little know that there is some issue when deploying that well it's with customize and because it's so big when you want to parameterize for different environments for production there is just a lot of work so there is this along issue that was uh opened like I think six years ago about kilohard uh but there was um much interest but not too much development and then um in rush we also thought hey we have many different projects inside our company that also use CubeFlow and wouldn't it be perfect if we could like simplify some stuff um maybe streamline some deployments and enable like proper parameterization so you can connect that to infrastructure as code tools and just propagate the variables secrets whatever right um so I started leading that with uh some assumptions and the basic assumption was that this helm chart should only focus on the main components.

So in the customize you have everything like search manager there's a lot and uh here we wanted to focus on just the basics because in bigger environments on corporate projects where people already know how to deploy stuff like manager or whatever they often just want to do it do it themselves because they also have to care for some company policies or maybe maybe cube play would be just one part of the bigger picture right so you want to have flexibility and this was uh these were the basic assumptions. So this is just a list of what's included um as you see the base components or or the main components and some of the supporting integration manifests. So some virtual services uh some gateways allow to proxy integration stuff K native and so on and because the CRDs for cubeflow are so big there is a separate helm chart for that as well and uh so what can you gain with this assumption as I mentioned the infrastructure as code um staff so everything clicks together for me it's very important and talking with many people's many different projects inside rush and outside we often share the same approach.

Um so if it this is something that can be connected to infrastructure as code setup uh you can integrate with cloud providers because you have some um parameterization there
