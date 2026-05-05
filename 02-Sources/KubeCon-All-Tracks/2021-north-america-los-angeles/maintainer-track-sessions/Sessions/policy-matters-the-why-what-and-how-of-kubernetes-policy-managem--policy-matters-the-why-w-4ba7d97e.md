---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Jayashree Ramanathan", "RedHat", "Aradhna Chetal", "TIAA", "Jim Bugwadia", "Nirmata", "Robert Ficcaglia", "SunStone Secure"]
sched_url: https://kccncna2021.sched.com/event/lV6b/policy-matters-the-why-what-and-how-of-kubernetes-policy-management-jayashree-ramanathan-redhat-aradhna-chetal-tiaa-jim-bugwadia-nirmata-robert-ficcaglia-sunstone-secure
youtube_search_url: https://www.youtube.com/results?search_query=Policy+Matters%21+The+Why%2C+What%2C+and+How+of+Kubernetes+Policy+Management+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Policy Matters! The Why, What, and How of Kubernetes Policy Management - Jayashree Ramanathan, RedHat; Aradhna Chetal, TIAA; Jim Bugwadia, Nirmata; Robert Ficcaglia, SunStone Secure

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Jayashree Ramanathan, RedHat, Aradhna Chetal, TIAA, Jim Bugwadia, Nirmata, Robert Ficcaglia, SunStone Secure
- Schedule: https://kccncna2021.sched.com/event/lV6b/policy-matters-the-why-what-and-how-of-kubernetes-policy-management-jayashree-ramanathan-redhat-aradhna-chetal-tiaa-jim-bugwadia-nirmata-robert-ficcaglia-sunstone-secure
- Busca YouTube: https://www.youtube.com/results?search_query=Policy+Matters%21+The+Why%2C+What%2C+and+How+of+Kubernetes+Policy+Management+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Policy Matters! The Why, What, and How of Kubernetes Policy Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6b/policy-matters-the-why-what-and-how-of-kubernetes-policy-management-jayashree-ramanathan-redhat-aradhna-chetal-tiaa-jim-bugwadia-nirmata-robert-ficcaglia-sunstone-secure
- YouTube search: https://www.youtube.com/results?search_query=Policy+Matters%21+The+Why%2C+What%2C+and+How+of+Kubernetes+Policy+Management+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6s3tc9QGxDo
- YouTube title: Policy Matters! The Why, What, and How of Kubernetes Policy Management
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/policy-matters-the-why-what-and-how-of-kubernetes-policy-management/6s3tc9QGxDo.txt
- Transcript chars: 24382
- Keywords: policy, policies, security, management, controls, practices, control, governance, important, compliance, customers, application, obviously, seeing, clusters, cluster, threats, course

### Resumo baseado na transcript

hello everyone this is the kubecon session policy matters why what and how of kubernetes policy management we've got uh jaya ramanathan radha chatal and jim bagwadia with us today to talk about all things policy uh why don't we start with some brief introductions radna good afternoon all my name is i manage the cloud security team at tiaa and also i'm the co-chair for cncf um technical advisory group thank you yeah thanks hi everyone um my name is jaya ramanathan i am a distribution engineer at red

### Excerpt da transcript

hello everyone this is the kubecon session policy matters why what and how of kubernetes policy management we've got uh jaya ramanathan radha chatal and jim bagwadia with us today to talk about all things policy uh why don't we start with some brief introductions radna good afternoon all my name is i manage the cloud security team at tiaa and also i'm the co-chair for cncf um technical advisory group thank you yeah thanks hi everyone um my name is jaya ramanathan i am a distribution engineer at red hat and focused on security and governance are really excited to be here because this policy management is one of my uh passion topics at this point oh dear jim hey everyone this is jim beguardia co-founder and ceo at nermata and i'm also a maintainer in caverno hi and i'm robert vicalia i'm a policy work group co-chair also volunteer with the cncf security tag and cto at sunstone so the policy work group we are focused on all things policy but specifically looking at communities policy itself and how kubernetes operators can use policy as code we have two current projects uh but before we talk about that just some infrastructure logistics we meet every other wednesday 8 a.m pacific we have our own slack channel and here's a link to our github repository where we have some of the prototypes uh jim's gonna talk about next yeah so one of the efforts and initiatives we're you know leading in the policy working group is creating a common way of reporting policy reports right so one thing we found is as as kubernetes policies become increasingly important for production deployments there are several policy tools and different tools have different languages uh perhaps different features but what seemed to be missing and something which we felt could be common is a way of reporting results from these policy engines so the policy report crd is that effort and working with the community we have now several tools like kiverno coop bench falco and others supporting the policy report there's more you know integrations and adapters in progress uh and we continue to sort of expand um other you know the outreach and projects that can work with the policy report yeah and we're absolutely looking for for more projects to incorporate into the uh the policy report crd process so jaya maybe you we we've been working on this policy white paper for now for for a little bit of time uh maybe you could give us a brief intro on the what and how is that we've been discussing in this white
