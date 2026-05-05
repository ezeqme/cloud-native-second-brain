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
speakers: ["Ammar Yasser", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFws/project-lightning-talk-beyond-guardrails-resource-lifecycle-automation-with-kyverno-ammar-yasser-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Beyond+Guardrails%3A+Resource+Lifecycle+Automation+With+Kyverno+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Beyond Guardrails: Resource Lifecycle Automation With Kyverno - Ammar Yasser, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ammar Yasser, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFws/project-lightning-talk-beyond-guardrails-resource-lifecycle-automation-with-kyverno-ammar-yasser-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Beyond+Guardrails%3A+Resource+Lifecycle+Automation+With+Kyverno+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Beyond Guardrails: Resource Lifecycle Automation With Kyverno.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFws/project-lightning-talk-beyond-guardrails-resource-lifecycle-automation-with-kyverno-ammar-yasser-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Beyond+Guardrails%3A+Resource+Lifecycle+Automation+With+Kyverno+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=F9AwR41FzGo
- YouTube title: Project Lightning Talk: Beyond Guardrails: Resource Lifecycle Automation With Kyverno - Ammar Yasser
- Match score: 1.007
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-beyond-guardrails-resource-lifecycle-automation/F9AwR41FzGo.txt
- Transcript chars: 4080
- Keywords: policy, policies, basically, namespace, resources, everything, delete, create, guardrails, resource, automation, everyone, maintainer, explain, keveno, blocking, request, platform

### Resumo baseado na transcript

Um I'm a maintainer for Keano and today I'm stepping in for Amaya sir who worked on that. Sadly could not come to CubeCon so yeah I'm replacing him and um I'm going to explain to you how like most teams use Keveno for blocking bad configs basically. top of that it comes also with integrated reporting uh fine grain exceptions and uh basically it's built for Kubernetes but in the recent versions we've been working to to get it out of Kubernetes for authorization and for other stuff like that as well.

### Excerpt da transcript

Yeah. So, hi everyone. Yeah. My name is uh Luke Mowski. Um I'm a maintainer for Keano and today I'm stepping in for Amaya sir who worked on that. Sadly could not come to CubeCon so yeah I'm replacing him and um I'm going to explain to you how like most teams use Keveno for blocking bad configs basically. Um but since the latest updates uh Keveno can do far more than just blocking stuff. And uh to explain all of that I will use um namespace as a service as an example. So the examp the the problem we have is um we like namespace as an as a service sorry uh you want to create ephemeral namespaces uh to test your pull request right so you create namespace uh but you want as a platform engineer you want to follow all the best practices as well as creating intermediate resources and maybe clean up when the pull request is done. Um, and the natural solution to do that will be to use a custom controller, you know. Um, so it will watch name spaces and do what we just talked about. But, um, in the end, you're going to have also to make it scalable depending on your infrastructure, monitoring it, probably adding reporting and all of that on the long term uh, becomes a real uh, engineering tool, you know.

So, this is where Keano comes in. Um, Kano for those who don't know is a project um like a we are a policy engine based on YAML and cell and what we do is we handle as I said validation but we handle much more things uh than that uh on top of that it comes also with integrated reporting uh fine grain exceptions and uh basically it's built for Kubernetes but in the recent versions we've been working to to get it out of Kubernetes for authorization and for other stuff like that as well. Um, so I was talking about the new policy. The first one we introduced in 117 uh like made made stable in 117 was the mutating policy. Um, basically it's here to mutate your resources before they eat etc. So the cubernetes database and uh what's going to do is like it's going to change everything uh to make sure it complies with your uh requirements. Um those policies those policies will allow you as well not just to mitate the name space that was created but all the underlying resources as well. Um so this is a big plus compared to some other policies like native policies in cube and things like that.

Um, another policy that we introduced is the generating policy. So, we talked about generating resources like network uh policies, world bindings. Uh, this is the policy you want to use
