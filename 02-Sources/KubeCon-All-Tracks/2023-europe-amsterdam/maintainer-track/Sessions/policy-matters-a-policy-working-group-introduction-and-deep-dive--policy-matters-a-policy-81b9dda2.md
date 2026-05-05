---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Jim Bugwadia", "Nirmata", "Frank Jogeleit", "LOVOO"]
sched_url: https://kccnceu2023.sched.com/event/1HzcK/policy-matters-a-policy-working-group-introduction-and-deep-dive-jim-bugwadia-nirmata-frank-jogeleit-lovoo
youtube_search_url: https://www.youtube.com/results?search_query=Policy+Matters%21+A+Policy+Working+Group+Introduction+and+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Policy Matters! A Policy Working Group Introduction and Deep Dive - Jim Bugwadia, Nirmata & Frank Jogeleit, LOVOO

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jim Bugwadia, Nirmata, Frank Jogeleit, LOVOO
- Schedule: https://kccnceu2023.sched.com/event/1HzcK/policy-matters-a-policy-working-group-introduction-and-deep-dive-jim-bugwadia-nirmata-frank-jogeleit-lovoo
- Busca YouTube: https://www.youtube.com/results?search_query=Policy+Matters%21+A+Policy+Working+Group+Introduction+and+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Policy Matters! A Policy Working Group Introduction and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HzcK/policy-matters-a-policy-working-group-introduction-and-deep-dive-jim-bugwadia-nirmata-frank-jogeleit-lovoo
- YouTube search: https://www.youtube.com/results?search_query=Policy+Matters%21+A+Policy+Working+Group+Introduction+and+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OFKQITURhfs
- YouTube title: Policy Matters! A Policy Working Group Introduction and Deep Dive - Jim Bugwadia & Frank Jogeleit
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/policy-matters-a-policy-working-group-introduction-and-deep-dive/OFKQITURhfs.txt
- Transcript chars: 26943
- Keywords: policy, policies, working, results, security, reports, management, cluster, compliance, report, course, within, configuration, resources, integration, reporter, itself, clusters

### Resumo baseado na transcript

So today we're going to talk about kubernetes policy management so a few topics we want to cover in this session first we're going to talk about why in a policy management matters for kubernetes where does it fit in the overall ecosystem we're going to also Deep dive into what the policy working group which is the cncf kubernetes working group does and then we'll you know talk we'll spend half of the session talking about the policy reporting API that was created in the working group and also

### Excerpt da transcript

So today we're going to talk about kubernetes policy management so a few topics we want to cover in this session first we're going to talk about why in a policy management matters for kubernetes where does it fit in the overall ecosystem we're going to also Deep dive into what the policy working group which is the cncf kubernetes working group does and then we'll you know talk we'll spend half of the session talking about the policy reporting API that was created in the working group and also talk about policy reporter which is an open source tool which you can use for reporting monitoring and management of policy results so first quick introductions I'm Jim mcguardia co-founder and CEO at nirmata we are the creators of caverno which is an open source policy engine also a cncf project I also co-chair in the policy working group in the kubernetes community and why I'm a maintainer of Kevin yeah welcome also from my side I'm Frank I'm a senior software engineer at levu a german-based dating platform I'm also the Creator and maintainer of policy reporter and open source contributor to tools like Carbono as well as FICO it's a quick notification about the cncf code of conduct so if you haven't read it it's available online use a QR code also you know for virtual attendees there's closed captioning available and you know for session q a you can enter in you know questions on the chat we will be answering after the session or of course as we have time in the live audience we'll also take questions there and thanks to our sponsor for the recording itself all right so diving into it let's start with what policies are and how they fit into kubernetes so in real life we all know policies as a form a set of rules which helps us Governor manage things within an organization like within your company you might have a vacation policy or other policies which are just established but in the software World policies are a form of configuration management So within configuration management itself you know you have the ability for some config like meta configuration to manage either other configurations or runtime behaviors of your systems so really as an operator as an OP steam or a platform team using policies you're setting rules to govern the behaviors as well as other configurations within your clusters and environments so in kubernetes of course we've all you know familiar with things like Network policies that's an example of a policy object which is baked right in into
