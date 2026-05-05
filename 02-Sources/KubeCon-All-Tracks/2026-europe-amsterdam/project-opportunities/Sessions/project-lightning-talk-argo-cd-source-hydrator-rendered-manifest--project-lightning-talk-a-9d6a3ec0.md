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
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Michael Crenshaw", "Lead Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxY/project-lightning-talk-argo-cd-source-hydrator-rendered-manifests-made-easy-michael-crenshaw-lead-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Argo+CD+Source+Hydrator%3A+Rendered+Manifests+Made+Easy%21+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Argo CD Source Hydrator: Rendered Manifests Made Easy! - Michael Crenshaw, Lead Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Michael Crenshaw, Lead Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxY/project-lightning-talk-argo-cd-source-hydrator-rendered-manifests-made-easy-michael-crenshaw-lead-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Argo+CD+Source+Hydrator%3A+Rendered+Manifests+Made+Easy%21+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Argo CD Source Hydrator: Rendered Manifests Made Easy!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxY/project-lightning-talk-argo-cd-source-hydrator-rendered-manifests-made-easy-michael-crenshaw-lead-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Argo+CD+Source+Hydrator%3A+Rendered+Manifests+Made+Easy%21+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Lkik-mrYfP4
- YouTube title: Project Lightning Talk: Argo CD Source Hydrator: Rendered Manifests Made Easy! - Michael Crenshaw
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-argo-cd-source-hydrator-rendered-manifests-made/Lkik-mrYfP4.txt
- Transcript chars: 5193
- Keywords: argo, source, manifests, manifest, hydrator, intuit, called, rendered, feature, hydrated, pattern, gitops, change, render, kustomize, understand, literally, additional

### Resumo baseado na transcript

I am a senior staff software engineer at Intuit and a lead maintainer for Argo Project, specifically Argo CD. And today, I'm just going to talk about one relatively recent feature called Argo CD source hydrator that simplifies the rendered manifest pattern for GitOps users. You can go back and say, "Okay, this is exactly what was deployed and this is where the problem came from." And of course, it still relies on the same old Argo CD code that's already really good at applying that code. And this gives you the opportunity to basically provide a gap where you can add additional automation, you can perform security checks, etc.

### Excerpt da transcript

My name is Michael Crenshaw. I am a senior staff software engineer at Intuit and a lead maintainer for Argo Project, specifically Argo CD. And today, I'm just going to talk about one relatively recent feature called Argo CD source hydrator that simplifies the rendered manifest pattern for GitOps users. So, pre-rendered manifest pattern GitOps was pretty straightforward. A user would make a change in Git and I just have an example here of someone bumping a dependency chart version in a chart.yaml. Argo CD would render those manifests using Helm, JSONet, Kustomize. We also support plugins. And then that manifest, which is flat and on the right side you see just a snippet of thousands and thousands of lines of YAML, that's what actually gets applied to the cluster. And the problem here is that middle section is kind of opaque to the user. That rendering happens, it goes out to the cluster. They don't necessarily really see or understand what's going on on the back end. So, the next evolution has been that people have shifted to the rendered manifest pattern where you make the exact same change, but then you have some process that runs Helm, Kustomize, etc.

And then pushes that to Git before finally handing it off to Argo CD to apply. And at that point, Argo CD's job is very simple. It's just sending out a flat manifest file. But the problem is you have to maintain that render column. That's custom internal code. At Intuit, it's Jenkins. We run Kustomize build and then push to Git. And it doesn't come with a lot of the niceties that Argo CD does. You don't have a beautiful UI necessarily. It doesn't retry on transitive network failures, things like that. So, we wanted to bring this column as a first class into Argo CD. And that's what we've done with the source hydrator feature. So again, same old same old on the left side, you're still just making a one-line change in a chart.yaml. Argo CD still does the exact same thing that it would usually do to render, but now it has the ability to push that rendered manifest to Git. And it's literally just a file called manifest.yaml. That's now available to users to read, understand what has changed between each iteration.

And if there are issues, you've got an audit trail. You can go back and say, "Okay, this is exactly what was deployed and this is where the problem came from." And of course, it still relies on the same old Argo CD code that's already really good at applying that code. So, enabling the feature is re
