---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Experience"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Mustafa Barış Ege", "Özge Aygül", "TÜBİTAK-BİLGEM"]
sched_url: https://kccnceu2026.sched.com/event/2CW86/from-jenkins-to-tekton-our-journey-toward-a-kubernetes-native-cicd-with-argocd-mustafa-baris-ege-ozge-aygul-tubitak-bilgem
youtube_search_url: https://www.youtube.com/results?search_query=From+Jenkins+to+Tekton%3A+Our+Journey+Toward+a+Kubernetes-Native+CI%2FCD+with+ArgoCD+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Jenkins to Tekton: Our Journey Toward a Kubernetes-Native CI/CD with ArgoCD - Mustafa Barış Ege & Özge Aygül, TÜBİTAK-BİLGEM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mustafa Barış Ege, Özge Aygül, TÜBİTAK-BİLGEM
- Schedule: https://kccnceu2026.sched.com/event/2CW86/from-jenkins-to-tekton-our-journey-toward-a-kubernetes-native-cicd-with-argocd-mustafa-baris-ege-ozge-aygul-tubitak-bilgem
- Busca YouTube: https://www.youtube.com/results?search_query=From+Jenkins+to+Tekton%3A+Our+Journey+Toward+a+Kubernetes-Native+CI%2FCD+with+ArgoCD+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Jenkins to Tekton: Our Journey Toward a Kubernetes-Native CI/CD with ArgoCD.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW86/from-jenkins-to-tekton-our-journey-toward-a-kubernetes-native-cicd-with-argocd-mustafa-baris-ege-ozge-aygul-tubitak-bilgem
- YouTube search: https://www.youtube.com/results?search_query=From+Jenkins+to+Tekton%3A+Our+Journey+Toward+a+Kubernetes-Native+CI%2FCD+with+ArgoCD+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=g7WXxziISCU
- YouTube title: From Jenkins to Tekton: Our Journey Toward a Kubernetes-Native CI... Mustafa Barış Ege & Özge Aygül
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-jenkins-to-tekton-our-journey-toward-a-kubernetes-native-ci-cd-wi/g7WXxziISCU.txt
- Transcript chars: 15808
- Keywords: pipeline, tekton, argo, pipelines, jenkins, course, needed, running, changes, architecture, developers, webhook, trigger, whatever, create, common, notification, automatically

### Resumo baseado na transcript

Today we are going to talk about Jenkins to Tekton, our journey towards a Kubernetes native CI/CD with Argo CD. It's a story about migration, sure, but mostly it's a story about moving our mindset from managing servers to managing pipelines. We really realized that we had Kubernetes applications and cloud native applications but we had static agents running in the build time. Also, we needed a Kubernetes API control tool because we don't want to manage the role-based access controls or securities etc. Firstly, I want to mention that Tekton use unified pipeline architecture which means we have one pipeline and one webhook and we can build our projects with that and it allows decoupled logic meaning that this pipeline logic separated from the implementation details. Also, Tekton is Kubernetes uses Kubernetes native secrets and role-based access mechanism.

### Excerpt da transcript

Hello everyone. Welcome to our presentation. Today we are going to talk about Jenkins to Tekton, our journey towards a Kubernetes native CI/CD with Argo CD. Thank you for joining us. Today we want to share journey. It's a story about migration, sure, but mostly it's a story about moving our mindset from managing servers to managing pipelines. We start with our journey began and we evolving this CI factory and we talk about how we met Tekton. After that we explain the Kubernetes way of CI/CD and go through the technical strategy. We briefly talk about our CI architecture and our CD architecture with the Argo CD and the image updater. We will continue with the cultural challenges and lesson we learned. After that we wrap up with a live demo. I am Ozge. And I'm Baris. >> [sighs] >> We are a team working We are a DevOps team working with generally Kubernetes and cloud native technologies. Our goal is not just to run pipelines but building our mindset. Sorry, I'm so excited. >> [laughter] >> Thank you. >> [applause] >> Our goal is just not run pipelines but to build sustainable, scalable and standardized delivery process to feel our developers sleep well at night but understand how we got there.

Baris is going to show you how our nightmares used to look like. All right. We had a similar Jenkins structure as you all know and love. We all love Jenkins, of course. It was fine at first because we had like four repositories or something like that which was fine. But in whenever the repos grow and teams get got larger, we needed something better. We had problems with the Jenkins. Of course Jenkins is a great tool, we all know it. I'm just repeating myself. But we had some frictions about [snorts] the Jenkins. First, of course, we had scalability issues. The static agents couldn't handle bursts loads loads efficiently. And we had management problems as well. We had plugin hell as we say which caused a lot of trouble for us. We had a lot of plugins which were kind of good sometimes but with the upgrades and etc. It was a it became a full-time job. And also we had a consistency problems. Something some some like we had like a lot of repositories in Jenkins files and the Jenkins files needed to be changed.

Whenever we changed the Jenkins files, the Jenkins file should be go to the PR stage and we needed to approve that etc. So this was a huge problem for us. Now, what we what we go to the next stage. We really realized that we had Kubernetes applications and cloud nati
