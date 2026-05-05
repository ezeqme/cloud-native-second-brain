---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Sonny Shi", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d5I/project-lightning-talk-invisible-finops-and-compliance-shift-left-with-cloud-custodian-sonny-shi-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Invisible+FinOps+and+Compliance%3A+Shift+Left+With+Cloud+Custodian+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Invisible FinOps and Compliance: Shift Left With Cloud Custodian - Sonny Shi, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Sonny Shi, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d5I/project-lightning-talk-invisible-finops-and-compliance-shift-left-with-cloud-custodian-sonny-shi-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Invisible+FinOps+and+Compliance%3A+Shift+Left+With+Cloud+Custodian+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Invisible FinOps and Compliance: Shift Left With Cloud Custodian.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5I/project-lightning-talk-invisible-finops-and-compliance-shift-left-with-cloud-custodian-sonny-shi-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Invisible+FinOps+and+Compliance%3A+Shift+Left+With+Cloud+Custodian+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PDkkn5ct_Ek
- YouTube title: Project Lightning Talk: Invisible FinOps and Compliance: Shift Left With Cloud Custodian - Sonny Shi
- Match score: 1.025
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-invisible-finops-and-compliance-shift-left-with/PDkkn5ct_Ek.txt
- Transcript chars: 5019
- Keywords: policy, policies, resources, action, create, optimization, compliance, resource, thousands, actually, enforcement, against, instance, invisible, custodian, shifting, imagine, basically

### Resumo baseado na transcript

I'm head of product at stacklet and a maintainer on the cloud consing project. Uh so today we're talking about invisible phups uh compliance and uh shifting left. Uh these policies run automatically in your environment constantly optimizing and taking action and they're acting invisibly but driving better outcomes for PHOPS security and compliance.

### Excerpt da transcript

Uh I'm Sonia. I'm head of product at stacklet and a maintainer on the cloud consing project. Uh so today we're talking about invisible phups uh compliance and uh shifting left. So to start uh every time you create a resource in the cloud you can imagine you're somewhere along this curve of time and spend right. So when you create it resource probably costs like basically nothing. Uh but as you go on uh you know and create resources, these cloud resources often have tens, hundreds or thousands of different ways that you can that you can configure a resource. Uh and each one of these can put you on one of many different uh timelines in terms of uh your cloud spend. Uh our goal is to avoid the bad timeline. So the one where you're spending the most amount of money um and you're overutilized. And sometimes we do that by finding optimization opportunities. So in this case maybe we're overprovisioned for the workload we're running on these resources and we find an optimization opportunity here. Uh next you can imagine that we draw another line uh and this is where we've made that optimization now we can lower that spend.

Uh you may create some form of ticket on your ticketing system. Uh but a lot of times it takes a lot of uh there's quite a bit of lag in between when that tick gets created uh when that optimization opportunity is uh detected and when you know someone goes and actually takes an action on that finding. Uh we categorize everything under that curve as waste. So this is both waste in terms of time and money. Uh but of course uh the waste isn't a trivial amount of money. Oftent times this can be tens of thousands, hundreds of thousands of dollars a year. Um, and the real question is, you know, how do we shift all of these things over to the left? So, we do this through policy. Uh, so policy is a declarative rule that defines what your cloud environment should be. It's uh with automated enforcement and in real time. Uh, and a policy with no enforcement really is a just a suggestion and suggestions often lead to inaction. Uh, if we look back at our graph, we can implement a cloud consigning policy drastically shifting all the action to the left.

So you know here we have a policy. Uh what we're saying is we want to find instances that are underutilized and we want to take action immediately. Uh the policy here is uh you know pretty easy to understand if you've never seen a policy before. You have a set of filters. Uh here we're saying you know uh reso
