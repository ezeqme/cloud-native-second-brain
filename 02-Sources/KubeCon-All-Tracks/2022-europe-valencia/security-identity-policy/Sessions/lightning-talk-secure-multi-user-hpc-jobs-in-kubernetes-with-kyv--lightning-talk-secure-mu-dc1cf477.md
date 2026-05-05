---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Trey Dockendorf", "Ohio Supercomputer Center"]
sched_url: https://kccnceu2022.sched.com/event/ytws/lightning-talk-secure-multi-user-hpc-jobs-in-kubernetes-with-kyverno-trey-dockendorf-ohio-supercomputer-center
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Secure+Multi+User+HPC+Jobs+in+Kubernetes+with+Kyverno+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Lightning Talk: Secure Multi User HPC Jobs in Kubernetes with Kyverno - Trey Dockendorf, Ohio Supercomputer Center

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Trey Dockendorf, Ohio Supercomputer Center
- Schedule: https://kccnceu2022.sched.com/event/ytws/lightning-talk-secure-multi-user-hpc-jobs-in-kubernetes-with-kyverno-trey-dockendorf-ohio-supercomputer-center
- Busca YouTube: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Secure+Multi+User+HPC+Jobs+in+Kubernetes+with+Kyverno+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Lightning Talk: Secure Multi User HPC Jobs in Kubernetes with Kyverno.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytws/lightning-talk-secure-multi-user-hpc-jobs-in-kubernetes-with-kyverno-trey-dockendorf-ohio-supercomputer-center
- YouTube search: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Secure+Multi+User+HPC+Jobs+in+Kubernetes+with+Kyverno+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MpbxRL8XPJ8
- YouTube title: Lightning Talk: Secure Multi User HPC Jobs in Kubernetes with Kyverno - Trey Dockendorf
- Match score: 0.975
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/lightning-talk-secure-multi-user-hpc-jobs-in-kubernetes-with-kyverno/MpbxRL8XPJ8.txt
- Transcript chars: 4124
- Keywords: policies, access, kyverno, mostly, kyberno, policy, communities, resources, on-demand, directories, ensure, running, namespace, prefix, config, validate, secure, little

### Resumo baseado na transcript

hi i'm trade off north of the ohio state computer center and this is secure multi-user hpc jobs and kubernetes with kyverno um a little bit to describe our hpc workload using kubernetes it's mostly lightweight interactive workloads so they have minimal cpu requirements compared tradition compared to traditional hpc right now it's mostly jupiter in our studio this is serving up numerous classrooms being used by distance learning um quick overview the technologies we're using so open on demand is how we make the hpc jobs or how we

### Excerpt da transcript

hi i'm trade off north of the ohio state computer center and this is secure multi-user hpc jobs and kubernetes with kyverno um a little bit to describe our hpc workload using kubernetes it's mostly lightweight interactive workloads so they have minimal cpu requirements compared tradition compared to traditional hpc right now it's mostly jupiter in our studio this is serving up numerous classrooms being used by distance learning um quick overview the technologies we're using so open on demand is how we make the hpc jobs or how we submit them to kubernetes it's essentially a web portal for hpc access a key part is it runs the web process runs as the user logged in to the hpc system supports multiple resource managers like slurm torque and kubernetes then there's uh kyberno which is a kubernetes policy engine you deploy policies using communities native resources and these policies we'll go over a little bit some of the challenges was supporting hpc jobs and kubernetes we wanted to treat the jobs similar to traditional hpc jobs and allow on-demand apps to submit to both slurm and kubernetes uh because communities pods can run as root um that made that presented challenges for shared file system access like gps or nfs home directories uh and we had to ensure that the users processes running in the pod were all being run as that user's uid and gids this was a big part of this was mainly to treat them uh as them for the file system access um some design patterns uh all user pods are in a namespace with user dash prefix um and then their username these namespaces are bootstrapped by on demand when you log into ondemand there's also roles and access controls um given to them in their namespace to allow them to do just enough to run on-demand jobs on the uh as both on a managed pc jobs um communities itself authenticates with our key cloud idp and uh the oauth the oidc tokens for on-demand are allowed to use the kubernetes thanks to an oauth2 audience uh we deployed a tool we wrote called kldap config map so this maps ldap data into config maps that can be used by kyverno so policy solutions with kyberno we have policies to ensure a uid and gid and supplemental groups of a pod match a user's ldap record we have policies to restrict host host path access amount locations to paths we want them to have access to such as nanotest home directories gpfs and some files for slurm we disallow all forms of privilege escalation we also enforce max resource requests and max ru
