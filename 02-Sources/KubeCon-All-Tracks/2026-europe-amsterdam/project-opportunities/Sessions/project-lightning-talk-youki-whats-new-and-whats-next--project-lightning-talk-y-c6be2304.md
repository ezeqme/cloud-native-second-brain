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
themes: ["AI ML"]
speakers: ["Yusuke Sakurai", "Reviewer"]
sched_url: https://kccnceu2026.sched.com/event/2HGVh/project-lightning-talk-youki-whats-new-and-whats-next-yusuke-sakurai-reviewer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+youki%3A+What%E2%80%99s+New+and+What%E2%80%99s+Next%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: youki: What’s New and What’s Next? - Yusuke Sakurai, Reviewer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yusuke Sakurai, Reviewer
- Schedule: https://kccnceu2026.sched.com/event/2HGVh/project-lightning-talk-youki-whats-new-and-whats-next-yusuke-sakurai-reviewer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+youki%3A+What%E2%80%99s+New+and+What%E2%80%99s+Next%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: youki: What’s New and What’s Next?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HGVh/project-lightning-talk-youki-whats-new-and-whats-next-yusuke-sakurai-reviewer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+youki%3A+What%E2%80%99s+New+and+What%E2%80%99s+Next%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=L4AgLkGk_T8
- YouTube title: Project Lightning Talk: youki: What’s New and What’s Next? - Yusuke Sakurai, Reviewer
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-youki-whats-new-and-whats-next/L4AgLkGk_T8.txt
- Transcript chars: 3676
- Keywords: runtime, compatibility, execution, specification, easier, updates, lanchi, support, matters, behavior, containers, update, recent, content, similar, already, features, devices

### Resumo baseado na transcript

Today I'd like to give a quick update on Yoki, what's new and what's next. In this talk, I'd briefly explain Yoki, what Yoki is, talk about some recent updates, and then look at a few load map items toward 1.0.0. And finally, bug fixes and security improvements include general stability bug and sh related fixes. That includes better compatibility, more flexible execution models, and easier Kubernetes adoption. So the goal here is to improve the compatibility with launch sheet especially in real world environments such as kubernetes kubernetes the next step is to continue aligning yi's behavior with ni and to san compatibility test coverage the second load map item is microbased Today adopting Yoki on Kubernetes still requires several other manual steps.

### Excerpt da transcript

Hello everyone. I'm Yusuke Sakai. I'm one of the maintenance of Yoki. Today I'd like to give a quick update on Yoki, what's new and what's next. In this talk, I'd briefly explain Yoki, what Yoki is, talk about some recent updates, and then look at a few load map items toward 1.0.0. First a very quick introduction. Yoki is an OCI runtime little in last. It is a lowle content runtime similar to runtimes like lanchi or shean. The project has around 7.3,000 GitHub stars and became a shen C shandbox project in October 2024. So Yoki is not just an experimental runtime anymore. It is growing as part of the BL cloud native runtime exist. Here are a few examples where Yoki is already being used. This shows where Yoki sits in the Kubernetes execution flow. Kubernetes does not invoke a low-level runtime directory. Instead, cubate talks to a C runtime such as content or kio which then invok time like s or yoki. So yi sits in at the low runtime layer. Now let's look at recent updates. First, new features. Yogi added support for net devices and Linux memory policy.

These are newer additions to the OCI runtime specification. Support for Net devices matters because newer Kubernetes networking models increasingly needed declarative attachment of network interfaces especially for AI, ML and other high performance workloads. The memory policy matters for numer workloads. Second, better compatibility. Yoki improved alignment with lanchi behavior and the OCI specification. Third, testing. The project has expanded OCI per conformance test and impatibility test. And finally, bug fixes and security improvements include general stability bug and sh related fixes. Above all, these updates shows that the project is steady becoming more practical and more reliable. Look ahead. The road map to Yoki 1.0.0 is really about making Yoki more practical for the adult use. That includes better compatibility, more flexible execution models, and easier Kubernetes adoption. First, the first road map item is improving compatibility with lanchi. Low level times are based on the OCI landtime specification.

However, real world compatibility requires more than spec compliance. Some commonly used features such as exec update and checkpoint are outside the specification and the runtime behavior can also define in certain ways. So the goal here is to improve the compatibility with launch sheet especially in real world environments such as kubernetes kubernetes the next step is to continue aligning yi'
