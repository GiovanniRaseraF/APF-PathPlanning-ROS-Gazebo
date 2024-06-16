# Specifiche di progetto
- Ambiente di sviluppo : ROS2 + Gazebo
- Simulatore drone Gazebo : (sjtu_drone/docker version)[https://github.com/GiovanniRaseraF/sjtu_drone_apf_speed_control]
- Algoritmo Path Planning: Artificial Potential Field

## Configurazione degli scenari:

1. movimento lungo percorso da un punto A ad un punto B senza ostacoli
2.  movimento lungo percorso da un punto A ad un punto B con ostacoli interposti
3. disposizione di target waypoint numerati in modo da realizzare un percorso in un ambiante tridimensionale,
con l'aggiunta di ulteriori ostacoli. La posizione dei waypoint può essere scelta arbitrariamente e il drone raggiunge i waypoint rispettandone l'ordine di numerazione. Le posizioni di waypoint e ostacoli sono fisse durante la simulazione.
4. come 3 ma con la disposizione dei waypoint numerati e degli ostacoli generata casualmente.  Le posizioni di waypoint e ostacoli sono fisse durante la simulazione e anche in questo caso il drone deve raggiungere i waypoint rispettandone l'ordine di numerazione.

5. [Opzionale] come 3 e 4 ma le posizioni di ostacoli e waypoint variano con continuità durante la simulazione con movimenti randomici e velocità inferiore rispetto a quella del drone

## Aggiornamenti
1. La simulazione non permette di leggere gli oggetti del mondo simulato, nemmeno tramite gz e ros bridge
