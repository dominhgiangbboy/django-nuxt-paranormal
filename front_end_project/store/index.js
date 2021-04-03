export const getters = {
    isAuthenticated(state) {
      return state.auth.loggedIn
    },
  
    loggedInUser(state) {
      return state.auth.user
    }
}

export const state = () => ({
  // Update button config
  disableUpdate:  false,
  hideUpdateButton: true,

  // Update button config
  disableCancel:  false,
  hideCancelButton: true,

  // Update button config
  disableInsert:  false,
  hideInsertButton: true,

  // Delete button config
  disableDelete:  false,
  hideDeleteButton: true,

  // Admin role
  isAdmin: true,

})
    
export const mutations = {
  // Update button config
  UPDATE_BUTTON(state, enable){
    state.disableUpdate = enable;
  },
  UPDATE_BUTTON_HIDE(state, hidden){
    state.hideUpdateButton = hidden;
  },
  // Cancel button config
  CANCEL_BUTTON(state, enable){
    state.disableCancel = enable;
  },
  CANCEL_BUTTON_HIDE(state, hidden){
    state.hideCancelButton = hidden;
  },
  // Insert button config
  INSERT_BUTTON(state, enable){
    state.disableInsert = enable;
  },
  INSERT_BUTTON_HIDE(state, hidden){
    state.hideInsertButton = hidden;
  },
   // Update button config
  DELETE_BUTTON(state, enable){
    state.disableDelete = enable;
  },
  DELETE_BUTTON_HIDE(state, hidden){
    state.hideDeleteButton = hidden;
  },
  //Store Role
  USER_ROLE(state, isAdmin){
    state.isAdmin = isAdmin;
  },
}