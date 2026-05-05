---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Augustin Husson", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyx/project-lightning-talk-perses-general-overview-augustin-husson-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Perses+General+Overview+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Perses General Overview - Augustin Husson, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Augustin Husson, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyx/project-lightning-talk-perses-general-overview-augustin-husson-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Perses+General+Overview+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Perses General Overview.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyx/project-lightning-talk-perses-general-overview-augustin-husson-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Perses+General+Overview+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fZYp4btZaTg
- YouTube title: Project Lightning Talk: Perses General Overview - Augustin Husson, Maintainer
- Match score: 0.853
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-perses-general-overview/fZYp4btZaTg.txt
- Transcript chars: 3462
- Keywords: perses, dashboard, providing, display, golang, plugins, github, deploy, directly, remote, general, overview, logs, profiling, aiming, number, sources, specification

### Resumo baseado na transcript

And well, since we don't have half of the audience that knows the the project, it's a great presentation. It's a observability visualization tool that is able to display any kind of signal today, metrics, logs, traces, and profiling.

### Excerpt da transcript

Hello everyone. My name is Augustin. I'm a Perses maintainer. I'm here to give you a general overview of Perses. And well, since we don't have half of the audience that knows the the project, it's a great presentation. Hello. Um so, what is Perses? Perses is a CNCF sandbox project. It's a observability visualization tool that is able to display any kind of signal today, metrics, logs, traces, and profiling. And we are aiming to increase the number of data sources supporting, such as Polar Signals for profiling or Open Search for the logs. It's also a an open dashboard solution, um which means we are providing specification for data dashboard and data sources in TypeScript, GoLang, and KuLang. And for Java, it's not yet published, but we are aiming to Uh this specification can be extensible with plugins. We are providing certain number of plugins in Perses/plugins repository. You can customize the validation of your dashboard to implement your own rules according to your governance of your company. And if you are not interested by an yet another application to display your monitoring, you can embed our components to display, for example, your time series chart.

We are providing components for that. It's in React, so probably you need to write your you are in React, but otherwise it's fine. Um it's also GitHub friendly. We are providing a CLI that you can use to validate your dashboards in a CI/CD. We are providing an operator to deploy Perses and CI/CDs as well, so you can deploy actually dashboard in your namespace. And you can use the Perses binary locally to well, when you are developing your dashboard, you can see in real time the effect of your dashboard directly before sending to production. Super straightforward to run Perses. So, now I just have to download the binary and run it, and that's it. We are also providing a dashboard as code workflow and framework. So, that means we are providing SDK in KuLang and GoLang. You can actually code your dashboard in GoLang, producing real code, and then it will produce a YAML or JSON files. Uh JSON that will be then validated by the CLI. You can create a preview if you have a remote remote instances that your CI/CD has access to.

And once the PR is merged, we can deploy your dashboard in the remote instances if you want. This workflow is only available with GitHub Actions for the moment, because well, it's easier for us to maintain GitHub Actions. But if you want to uh over support of CI/CD, let us know. The
