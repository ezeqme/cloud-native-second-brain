---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["GitOps Delivery"]
speakers: ["Mayank Kumar", "Andy Chen", "Salesforce"]
sched_url: https://kccncna2022.sched.com/event/182HL/how-salesforce-is-moving-from-spinnaker-to-argo-workflows-for-provisioning-add-ons-mayank-kumar-andy-chen-salesforce
youtube_search_url: https://www.youtube.com/results?search_query=How+Salesforce+Is+Moving+From+Spinnaker+To+Argo+Workflows+For+Provisioning+Add-Ons+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How Salesforce Is Moving From Spinnaker To Argo Workflows For Provisioning Add-Ons - Mayank Kumar & Andy Chen, Salesforce

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Mayank Kumar, Andy Chen, Salesforce
- Schedule: https://kccncna2022.sched.com/event/182HL/how-salesforce-is-moving-from-spinnaker-to-argo-workflows-for-provisioning-add-ons-mayank-kumar-andy-chen-salesforce
- Busca YouTube: https://www.youtube.com/results?search_query=How+Salesforce+Is+Moving+From+Spinnaker+To+Argo+Workflows+For+Provisioning+Add-Ons+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How Salesforce Is Moving From Spinnaker To Argo Workflows For Provisioning Add-Ons.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182HL/how-salesforce-is-moving-from-spinnaker-to-argo-workflows-for-provisioning-add-ons-mayank-kumar-andy-chen-salesforce
- YouTube search: https://www.youtube.com/results?search_query=How+Salesforce+Is+Moving+From+Spinnaker+To+Argo+Workflows+For+Provisioning+Add-Ons+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=r4IQ6u8u4A4
- YouTube title: How Salesforce is using ArgoWorkflows for provisioning add-ons - Mayank Kumar & Andy Chen
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-salesforce-is-moving-from-spinnaker-to-argo-workflows-for-provisio/r4IQ6u8u4A4.txt
- Transcript chars: 27256
- Keywords: workflow, pipelines, add-on, spinnaker, add-ons, clusters, workflows, argo, cluster, provisioning, owners, process, templates, number, deploy, native, environment, environments

### Resumo baseado na transcript

hi everyone I'm Andy I'm a software engineer on mines team and I'm also very excited to be here especially since it's my first ever cubecon together we are going to take you through our journey of improving the life cycle management and provisioning of add-ons across thousands of eks clusters in hyperforce using Argo workflows a little about Salesforce we are proud to be the number one CRM company we are also now the world's largest Enterprise apps company in addition to being a category leader we are also

### Excerpt da transcript

hi everyone I'm Andy I'm a software engineer on mines team and I'm also very excited to be here especially since it's my first ever cubecon together we are going to take you through our journey of improving the life cycle management and provisioning of add-ons across thousands of eks clusters in hyperforce using Argo workflows a little about Salesforce we are proud to be the number one CRM company we are also now the world's largest Enterprise apps company in addition to being a category leader we are also a leader in philanthropy addition Innovation and culture we believe that business is the greatest platform for Change and one of the ways we use our platform for change is through our 111 philanthropy model where we pledge one percent of our time equity and product to giving back to our communities a little about Salesforce and hyperforce you'll hear this word a lot in the next in the lot in the rest of the slides hyperforces are trusted Cloud platform it is the infrastructure built in public Cloud which is the foundation of everything we do on Salesforce I propose is secure by default and it provides comprehensive privacy standards that help you get control and transparency of your customers data a little introduction about our team we are the hyperforce kubernetes platform team we provide a multi substrate and completely manage kubernetes platform integrated with the rest of the Salesforce infrastructure our value propositions are we provide 24 7 support for our clusters and Integrations we manage all of the Salesforce infrastructure Integrations into kubernetes including certifying a new release continuous synthetic monitoring and safe rollout maintaining trust is our number one value at Salesforce we help maintain security and Trust by running the most up-to-date secure and patched version of kubernetes in hyperforce including integration versions by solving problems centrally in a platform we avoid dedicated cluster management head count which based on an internal surveys around one and a half Engineers per service team on an average our mission is to allow service owners which are other team members team at Salesforce to focus on the unique value of their services without having to focus on infrastructure this increases developer agility while decreasing operational cost and complexity as a result we need an efficient scalable and resilient system for managing our clusters and cluster components to achieve our mission so what are add-ons add-ons or
