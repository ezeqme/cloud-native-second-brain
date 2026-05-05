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
speakers: ["Khanh Tran", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyu/project-lightning-talk-pipecdv1-is-here-leverage-the-power-of-plugin-architecture-khanh-tran-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+PipeCDv1+Is+Here%21+Leverage+The+Power+Of+Plugin+Architecture+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: PipeCDv1 Is Here! Leverage The Power Of Plugin Architecture - Khanh Tran, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Khanh Tran, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyu/project-lightning-talk-pipecdv1-is-here-leverage-the-power-of-plugin-architecture-khanh-tran-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+PipeCDv1+Is+Here%21+Leverage+The+Power+Of+Plugin+Architecture+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: PipeCDv1 Is Here! Leverage The Power Of Plugin Architecture.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyu/project-lightning-talk-pipecdv1-is-here-leverage-the-power-of-plugin-architecture-khanh-tran-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+PipeCDv1+Is+Here%21+Leverage+The+Power+Of+Plugin+Architecture+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hO3xdy2fiK4
- YouTube title: Project Lightning Talk: PipeCDv1 Is Here! Leverage The Power Of Plugin Architecture - Khanh Tran
- Match score: 1.016
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-pipecdv1-is-here-leverage-the-power-of-plugin-a/hO3xdy2fiK4.txt
- Transcript chars: 4453
- Keywords: plug-in, platform, plugin, application, architecture, update, released, configuration, deployment, control, centric, interest, specific, config, documentation, engineer, provide, supported

### Resumo baseado na transcript

Um so for people who new to PICD basically PICD what's flexd and our CD do for for and for the other platform as well is an GOP style progressive delivery platform that provide consistent deployment and operation experience for any application platform. before v1 supported platform was communities terraform ECS lambda and GCP car run. The pipd and it plugin communicate via gpc protocol and user win control with plugin should be instant and uh config what is uh to do uh via the 5D configuration with the update of the 5D plug-in architecture.

### Excerpt da transcript

Hi everyone, I'm uh Kang. I'm software engineer at Season and I'm maintainer of the PIC project. Uh my talk is about the PICD project and some update from it. Um so for people who new to PICD basically PICD what's flexd and our CD do for for and for the other platform as well is an GOP style progressive delivery platform that provide consistent deployment and operation experience for any application platform. before v1 supported platform was communities terraform ECS lambda and GCP car run. So uh from an overview pd consist of uh two component the control plane and the agent we call is piped. The control plane is the centric component managed deployment data provide the RPC API to connect with pipd agent as well as the UI. While the pipd is a single binary, you can run uh it anywhere you want like in the port or seate task handler or anywhere. This architect have separate the platform and the dev team scope. And uh if you are a platform engineer and want a solution for centric CD for the whole company with a different platform like I said cumis lambda anything at the same time then you can consider pd for more about pd internal please check out the official website of pid.

So uh let's uh check out the update from project. Um we just released the PICD v1 at unfa state and is adopt the plug-in architecture in detail in interest of including all platform supporting code into the 5D as codebase and s it as a single binary. All the platform and state execution specific code is now separate from the 5D core. They are built separately and distribute as a plug-in of the pip agent. The pipd and it plugin communicate via gpc protocol and user win control with plugin should be instant and uh config what is uh to do uh via the 5D configuration with the update of the 5D plug-in architecture. We also rebuild the pcd app config abstraction. Uh you can see here on the left is the old pipd configuration file. Um for PI for a cumatis application it require a specific application guide that's tie correct with the platform like for kimis application it need to be kimotis app and um also we have an input spec that need to contain the field that fit all the pipe CD supported guide that lead to hard to follow documentation and implementation uh from our side and uh you can see on the right is the new 5D app configuration uh with Kai set to centric application and platform config will be moved under the plug-in specific will be easier for board dog and implementation.

Of course
